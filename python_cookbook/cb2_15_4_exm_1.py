class MyServer(SimpleXMLRPCServer.SimpleXMLRPCServer):
    def serve_forever(self):
	while running:
	    self.handle_request()
server = MyServer(('127.0.0.1', 8000))
server.register_function(finis)
server.serve_forever()
