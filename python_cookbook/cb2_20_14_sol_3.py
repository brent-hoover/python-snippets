class auto_attr(object):
    def __init__(self, name, factory, *a, **k):
        self.data = name, factory, a, k
    def __get__(self, obj, clas=None):
        name, factory, a, k = self.data
        setattr(obj, name, factory(*a, **k))
        return getattr(obj, name)
