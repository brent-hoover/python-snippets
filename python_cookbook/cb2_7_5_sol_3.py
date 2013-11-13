class picklable_boundmethod(object):
    def __init__(self, mt):
        self.mt = mt
    def __getstate__(self):
        return self.mt.im_self, self.mt.im_func.__name__
    def __setstate__(self, (s,fn)):
        self.mt = getattr(s, fn)
    def __call__(self, *a, **kw):
        return self.mt(*a, **kw)
