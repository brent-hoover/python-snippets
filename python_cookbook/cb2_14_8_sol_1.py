import httplib, base64, socket
# parameters for the script
user = 'proxy_login'; passwd = 'proxy_pass'
host = 'login.yahoo.com'; port = 443
phost = 'proxy_host'; pport = 80
# setup basic authentication
user_pass = base64.encodestring(user+':'+passwd)
proxy_authorization = 'Proxy-authorization: Basic '+user_pass+'\r\n'
proxy_connect = 'CONNECT %s:%s HTTP/1.0\r\n' % (host, port)
user_agent = 'User-Agent: python\r\n'
proxy_pieces = proxy_connect+proxy_authorization+user_agent+'\r\n'
# connect to the proxy
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.connect((phost, pport))
proxy_socket.sendall(proxy_pieces+'\r\n')
response = proxy_socket.recv(8192)
status = response.split()[1]
if status!='200':
    raise IOError, 'Connecting to proxy: status=%s' % status
# trivial setup for SSL socket
ssl = socket.ssl(proxy_socket, None, None)
sock = httplib.FakeSocket(proxy_socket, ssl)
# initialize httplib and replace the connection's socket with the SSL one
h = httplib.HTTPConnection('localhost')
h.sock = sock
# and finally, use the now-HTTPS httplib connection as you wish
h.request('GET', '/')
r = h.getresponse()
print r.read()
