# give the base class a short, readable nickname
from SimpleXMLRPCServer import SimpleXMLRPCServer as BaseServer
class Server(BaseServer):
    def __init__(self, host, port):
        # accept separate hostname and portnumber and group them
        BaseServer.__init__(self, (host, port))
    def server_bind(self):
        # allow fast restart of the server after it's killed
        import socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        BaseServer.server_bind(self)
    allowedClientHosts = '127.0.0.1', '192.168.0.15',
    def verify_request(self, request, client_address):
        # forbid requests except from specific client hosts
        return client_address[0] in self.allowedClientHosts
