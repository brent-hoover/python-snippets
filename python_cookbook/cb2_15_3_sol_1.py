# xmlrpc_server.py
from socket import gethostname
from medusa.xmlrpc_handler import xmlrpc_handler
from medusa.http_server import http_server
from medusa import asyncore
class xmlrpc_server(xmlrpc_handler):
    # initialize and run the server
    def __init__(self, host=None, port=8182):
        if host is None:
            host = gethostname()
        hs = http_server(host, port)
        hs.install_handler(self)
        asyncore.loop()
    # an example of a method to be exposed via the XML-RPC protocol
    def add(self, op1, op2):
        return op1 + op2
    # the infrastructure ("plumbing") to expose methods
    def call(self, method, params):
        print "calling method: %s, params: %s" % (method, params)
        if method == 'add':
            return self.add(*params)
        return "method not found: %s" % method
if __name__ == '__main__':
    server = xmlrpc_server()
