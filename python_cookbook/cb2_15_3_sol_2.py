# xmlrpc_client.py
from socket import gethostname
from xmlrpclib import Transport, dumps
class xmlrpc_connection(object):
    def __init__(self, host=None, port=8182):
        if host is None:
            host = gethostname()
        self.host = "%s:%s" % (host, port)
        self.transport = Transport()
    def remote(self, method, params=()):
        """ Invoke the server with the given method name and parameters.
            The return value is always a tuple. """
        return self.transport.request(self.host, '/RPC2',
                                      dumps(params, method))
if __name__ == '__main__':
    connection = xmlrpc_connection()
    answer, = connection.remote("add", (40, 2))
    print "The answer is:", answer
