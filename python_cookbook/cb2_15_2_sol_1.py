# Server code sxr_server.py
import SimpleXMLRPCServer
class StringFunctions(object):
    def __init__(self):
        # Make all the functions in Python's standard string module
        # available as 'python_string.func_name' for each func_name
        import string
        self.python_string = string
    def _privateFunction(self):
        # This function cannot be called directly through XML-RPC because
        # it starts with an underscore character '_', i.e., it's "private"
        return "you'll never get this result on the client"
    def chop_in_half(self, astr):
        return astr[:len(astr)/2]
    def repeat(self, astr, times):
        return astr * times
if __name__=='__main__':
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(StringFunctions())
    server.register_function(lambda astr: '_' + astr, '_string')
    server.serve_forever()
