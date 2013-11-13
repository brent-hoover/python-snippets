import inspect
def second_arg(func):
    args = inspect.getargspec(func)[0]
    try: return args[1]
    except IndexError: return None
def super_wrapper(cls, func):
    def wrapper(self, *args, **kw):
        return func(self, super(cls, self), *args, **kw)
    # 2.4 only: wrapper.__name__ = func.__name__
    return wrapper
class MetaCooperative(type):
    def __init__(cls, name, bases, dic):
        super(MetaCooperative, cls).__init__(cls, name, bases, dic)
        for attr_name, func in dic.iteritems():
            if inspect.isfunction(func) and second_arg(func) == "super":
                setattr(cls, attr_name, super_wrapper(cls, func)) 
class Cooperative:
    __metaclass__ = MetaCooperative
