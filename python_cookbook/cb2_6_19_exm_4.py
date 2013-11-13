import inspect
class Der(A, B, C, D):
    def met(self):
        s = super(Der, self)
        # get the superclass's bound-method object, or else None
        m = getattr(s, 'met', None)
        try:
            args, varargs, varkw, defaults = inspect.getargspec(m)
        except TypeError:
            # m is not a method, just ignore it
            pass
        else:
            # m is a method, do all its arguments have default values?
            if len(defaults) == len(args):
                # yes! so, call it:
                m()
        print 'met in Der'
