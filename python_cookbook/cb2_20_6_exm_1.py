def processedby(processor):
    """ decorator to wrap the processor around a function. """
    def processedfunc(func):
        def wrappedfunc(*args, **kwargs):
            return processor(func, *args, **kwargs)
        return wrappedfunc
    return processedfunc
