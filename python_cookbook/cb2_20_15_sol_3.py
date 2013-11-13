# optimize thyself!
_insert_constant = _make_constants(_insert_constant)
_make_constants = _make_constants(_make_constants)
import types
@_make_constants
def bind_all(mc, builtin_only=False, stoplist=(), verbose=False):
    """ Recursively apply constant binding to functions in a module or class.
    """
    try:
        d = vars(mc)
    except TypeError:
        return
    for k, v in d.items():
        if type(v) is types.FunctionType:
            newv = _make_constants(v, builtin_only, stoplist,  verbose)
            setattr(mc, k, newv)
        elif type(v) in (type, types.ClassType):
            bind_all(v, builtin_only, stoplist, verbose)
@_make_constants
def make_constants(builtin_only=False, stoplist=[], verbose=False):
    """ Call this metadecorator to obtain a decorator which optimizes
        global references by constant binding on a specific function.
    """
    if type(builtin_only) == type(types.FunctionType):
        raise ValueError, 'must CALL, not just MENTION, make_constants'
    return lambda f: _make_constants(f, builtin_only, stoplist, verbose)
