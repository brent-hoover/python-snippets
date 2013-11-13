for extname in 'spam', 'eggs':
    HandlerClass = importName("MyApp.extensions." + extname, "Handler")
    handler = HandlerClass()
    handler.handleSomething()
