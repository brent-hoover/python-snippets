import copy
def freshdefaults(f):
    "a decorator to wrap f and keep its default values fresh between calls"
    fdefaults = f.func_defaults
    def refresher(*args, **kwds):
        f.func_defaults = deepcopy(fdefaults)
        return f(*args, **kwds)
    # in 2.4, only: refresher.__name__ = f.__name__
    return refresher
# usage as a decorator, in python 2.4:
@freshdefaults
def packitem(item, pkg=[]):
    pkg.append(item)
    return pkg
# usage in python 2.3: after the function definition, explicitly assign:
# f = freshdefaults(f)
