import weakref, new
class ref(object):
    """ Wraps any callable, most importantly a bound method, in
        a way that allows a bound method's object to be GC'ed, while
        providing the same interface as a normal weak reference. """
    def __init__(self, fn):
        try:
            # try getting object, function, and class
            o, f, c = fn.im_self, fn.im_func, fn.im_class
        except AttributeError:                # It's not a bound method
            self._obj = None
            self._func = fn
            self._clas = None
        else:                                 # It is a bound method
            if o is None: self._obj = None    # ...actually UN-bound
            else: self._obj = weakref.ref(o)  # ...really bound
            self._func = f
            self._clas = c
    def __call__(self):
        if self.obj is None: return self._func
        elif self._obj() is None: return None
        return new.instancemethod(self._func, self.obj(), self._clas)
