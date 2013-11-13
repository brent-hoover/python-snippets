class chainable(object):
    def __init__(self, obj):
        self.obj = obj
    def __iter__(self):
        return iter(self.obj)
    def __getattr__(self, name):
        def proxy(*args, **kwds):
            result = getattr(self.obj, name)(*args, **kwds)
            if result is None: return self
            else: return result
        # 2.4 only: proxy.__name__ = name
        return proxy
