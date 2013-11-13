class attr(object):
    def __init__(self, factory, *a, **k):
        self.creation_data = factory, a, k
import inspect
def is_attr(member):
    return isinstance(member, attr)
class MetaAuto(type):
    def __call__(cls, *a, **k):
        obj = super(MetaAuto, cls).__call__(cls, *a, **k)
        # set all values for 'attr' attributes
        for n, v in inspect.getmembers(cls, is_attr):
            factory, a, k = v.creation_data
            setattr(obj, n, factory(*a, **k))
        return obj
# lets' let any class use our custom metaclass by inheriting from auto_object
class auto_object:
    __metaclass__ = MetaAuto
