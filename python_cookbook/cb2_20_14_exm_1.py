class smart_attr(object):
    name = None
    def __init__(self, factory, *a, **k):
        self.creation_data = factory, a, k
    def __get__(self, obj, clas=None):
        if self.name is None:
            raise RuntimeError, ("class %r uses a smart_attr, so its "
                "metaclass should be MetaSmart, but is %r instead" %
                (clas, type(clas)))
        factory, a, k = self.creation_data
        setattr(obj, name, factory(*a, **k))
        return getattr(obj, name)
class MetaSmart(type):
    def __new__(mcl, clasname, bases, clasdict):
        # set all names for smart_attr attributes
        for k, v in clasdict.iteritems():
            if isinstance(v, smart_attr):
                v.name = k
        # delegate the rest to the supermetaclass
        return super(MetaSmart, mcl).__new__(mcl, clasname, bases, clasdict)
# let's let any class use our custom metaclass by inheriting from smart_object
class smart_object:
    __metaclass__ = MetaSmart
