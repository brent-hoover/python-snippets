class Proxy(object):
    """ base class for all proxies """
    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        self._obj = obj
    def __getattr__(self, attrib):
        return getattr(self._obj, attrib)
def make_binder(unbound_method):
    def f(self, *a, **k): return unbound_method(self._obj, *a, **k)
    # in 2.4, only: f.__name__ = unbound_method.__name__
    return f
known_proxy_classes = {}
def proxy(obj, *specials):
    ''' factory-function for a proxy able to delegate special methods '''
    # do we already have a suitable customized class around?
    obj_cls = obj.__class__
    key = obj_cls, specials
    cls = known_proxy_classes.get(key)
    if cls is None:
        # we don't have a suitable class around, so let's make it
        cls = type("%sProxy" % obj_cls.__name__, (Proxy,), {})
        for name in specials:
            name = '__%s__' % name
            unbound_method = getattr(obj_cls, name)
            setattr(cls, name, make_binder(unbound_method))
        # also cache it for the future
        known_proxy_classes[key] = cls
    # instantiate and return the needed proxy
    return cls(obj)
