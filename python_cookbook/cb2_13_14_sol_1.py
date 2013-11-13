import threading, socket, traceback, sys, base64, time
def recv_all(the_socket, timeout=1):
    ''' receive all data available from the_socket, waiting no more than
        ``timeout'' seconds for new data to arrive; return data as string. '''
    # use non-blocking sockets
    the_socket.setblocking(0)
    total_data = []
    begin = time.time()
    while True:
        ''' loop until timeout '''
        if total_data and time.time()-begin > timeout:
            break     # if you got some data, then break after timeout seconds
        elif time.time()-begin > timeout*2:
            break     # if you got no data at all yet, wait a little longer
        try:
            data = the_socket.recv(4096)
            if data:
                total_data.append(data)
                begin = time.time()       # reset start-of-wait time
            else:
                time.sleep(0.1)           # give data some time to arrive
        except:
            pass
    return ''.join(total_data)
class thread_it(threading.Thread):
    ''' thread instance to run a tunnel, or a tunnel-client '''
    done = False
    def __init__(self, tid='', proxy='', server='', tunnel_client='', 
                 port=0, ip='', timeout=1):
        threading.Thread.__init__(self)
        self.tid = tid
        self.proxy = proxy
        self.port = port
        self.server = server
        self.tunnel_client = tunnel_client
        self.ip = ip; self._port = port
        self.data = {}     #   store data here to get later
        self.timeout = timeout
    def run(self):
        try:
            if self.proxy and self.server:
                ''' running tunnel operation, so bridge server <-> proxy '''
                new_socket = False
                while not thread_it.done:    # loop until termination
                    if not new_socket:
                        new_socket, address = self.server.accept()
                    else:
                        self.proxy.sendall(
                            recv_all(new_socket, timeout=self.timeout))
                        new_socket.sendall(
                            recv_all(self.proxy, timeout=self.timeout))
            elif self.tunnel_client:
                ''' running tunnel client, just mark down when it's done '''
                self.tunnel_client(self.ip, self.port)
                thread_it.done = True     # normal termination
        except Exception, error:
            print traceback.print_exc(sys.exc_info()), error
            thread_it.done = True         # orderly termination upon exception
class build(object):
    ''' build a tunnel object, ready to run two threads as needed '''
    def __init__(self, host='', port=443, proxy_host='', proxy_port=80, 
                 proxy_user='', proxy_pass='', proxy_type='', timeout=1):
        self._port=port; self.host=host; self._phost=proxy_host
        self._puser=proxy_user; self._pport=proxy_port; self._ppass=proxy_pass
        self._ptype=proxy_type; self.ip='127.0.0.1'; self.timeout=timeout
        self._server, self.server_port = self.get_server()
    def get_proxy(self):
        if not self._ptype:
            proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy.connect((self._phost, self._pport))
            proxy_authorization = ''
            if self._puser:
                proxy_authorization = 'Proxy-authorization: Basic '+\
                    base64.encodestring(self._puser+':'+self._ppass
                                       ).strip()+'\r\n'
            proxy_connect = 'CONNECT %s:%sHTTP/1.0\r\n' % (
                             self.host, self._port)
            user_agent = 'User-Agent: pytunnel\r\n'
            proxy_pieces = proxy_connect+proxy_authorization+user_agent+'\r\n'
            proxy.sendall(proxy_pieces+'\r\n')
            response = recv_all(proxy, timeout=0.5)
            status = response.split(None, 1)[1]
            if int(status)/100 != 2:
                print 'error', response
                raise RuntimeError(status)
            return proxy
    def get_server(self):
        port = 2222
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen(5)
        return server, port
    def run(self, func):
        Threads = []
        Threads.append(thread_it(tid=0, proxy=self.get_proxy(),
                                 server=self._server, timeout=self.timeout))
        Threads.append(thread_it(tid=1, tunnel_client=func, ip=self.ip,
                                 port=self.server_port, timeout=0.5))
        for Thread in Threads:
            Thread.start()
        for Thread in Threads:
            Thread.join()
