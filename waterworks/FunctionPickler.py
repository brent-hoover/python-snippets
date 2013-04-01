"""Allows you to create pickle-able references to functions.  Of course,
this is with the understanding that the underlying implementation of
that function can change, so don't use this if you require future-proof
results."""
from pickle import PicklingError

class PickledFunction:
    def __init__(self, function):
        if not callable(function):
            raise ValueError("Not callable: %r" % function)

        self.name = function.__name__
        if self.name == '<lambda>':
            raise ValueError("Function cannot be a lambda.")

        self.modulename = function.__module__
        if self.modulename == "__main__":
            import inspect, path
            modpath = path.path(inspect.getsourcefile(function))
            self.modulename = str(modpath.stripext().basename())

        try: # make sure we can find the function later
            self._import()
        except (KeyboardInterrupt, SystemExit): 
            raise
        except:
            raise PicklingError("Can't pickle function %r" % function)
    def __setstate__(self, state):
        self.__dict__.update(state)
        self._import()
    def _import(self):
        mod = __import__(self.modulename)
        self._func = getattr(mod, self.name)
    def __getstate__(self):
        state = dict(self.__dict__)
        state.pop('_func', None)
        return state

    def __getattr__(self, attr):
        """All attributes (__call__ especially) are passed onto the
        function."""
        return getattr(self._func, attr)

if __name__ == "__main__":
    import time
    import pickle

    func = time.time
    def func2():
        "Not pickle-able"
        return 'zarg2'

    p = PickledFunction(func)
    print 'p', p
    pickled = pickle.dumps(p)
    unpickled = pickle.loads(pickled)
    print 'unpickled', unpickled
    print 'doc', unpickled.__doc__
    print unpickled()
    print 'done'
