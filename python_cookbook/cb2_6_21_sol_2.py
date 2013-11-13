import inspect
class MetaAutoReloader(MetaInstanceTracker):
    ''' a metaclass which, when one of its classes is re-built, updates all
        instances and subclasses of the previous version to the new one '''
    def __init__(cls, name, bases, ns):
        # the new class may optionally define an __update__ method
        updater = ns.pop('__update__', None)
        super(MetaInstanceTracker, cls).__init__(name, bases, ns)
        # inspect locals & globals in the stackframe of our caller
        f = inspect.currentframe().f_back
        for d in (f.f_locals, f.f_globals):
            if name in d:
                # found the name as a variable is it the old class
                old_class = d[name]
                if not isinstance(old_class, mcl):
                    # no, keep trying
                    continue
                # found the old class: update its existing instances
                for instance in old_class.__instances__():
                    instance.__class__ = cls
                    if updater: updater(instance)
                    cls.__instance_refs__.append(weakref.ref(instance))
                # also update the old class's subclasses
                for subclass in old_class.__subclasses__():
                    bases = list(subclass.__bases__)
                    bases[bases.index(old_class)] = cls
                    subclass.__bases__ = tuple(bases)
                break
        return cls
class AutoReloader:
    ''' any class may subclass this one, to get automatic updates '''
    __metaclass__ = MetaAutoReloader
