import weakref
class MetaInstanceTracker(type):
    ''' a metaclass which ensures its classes keep track of their instances '''
    def __init__(cls, name, bases, ns):
        super(MetaInstanceTracker, cls).__init__(name, bases, ns)
        # new class cls starts with no instances
        cls.__instance_refs__ = []
    def __instances__(cls):
        ''' return all instances of cls which are still alive '''
        # get ref and obj for refs that are still alive
        instances = [(r, r()) for r in cls.__instance_refs__ if r() is not None]
        # record the still-alive references back into the class
        cls.__instance_refs__ = [r for (r, o) in instances]
        # return the instances which are still alive
        return [o for (r, o) in instances]
    def __call__(cls, *args, **kw):
        ''' generate an instance, and record it (with a weak reference) '''
        instance = super(MetaInstanceTracker, cls).__call__(*args, **kw)
        # record a ref to the instance before returning the instance
        cls.__instance_refs__.append(weakref.ref(instance))
        return instance
class InstanceTracker:
    ''' any class may subclass this one, to keep track of its instances '''
    __metaclass__ = MetaInstanceTracker
