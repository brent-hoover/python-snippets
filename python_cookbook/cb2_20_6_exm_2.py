class SomeClass(object):
    @processedby(tracing_processor)
    def amethod(self, s):
        return 'Hello, ' + s
