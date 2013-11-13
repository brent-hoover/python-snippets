import SimpleXMLRPCServer
running = True
def finis():
    global running
    running = False
    return 1
server = SimpleXMLRPCServer.SimpleXMLRPCServer(('127.0.0.1', 8000))
server.register_function(finis)
while running:
    server.handle_request()
