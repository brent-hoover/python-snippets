import inspect
from functools import partial

def autopartial(func):
    """
    Will make a function return a partial if not all the arguments are
    returned::

        >>> @autopartial
        ... def squares(x, y, z):
        ...     return x**2 + y**2 + z**2
        >>> squares(2, 3)
        <functools.partial object at ...>
        >>> squares(1, 2, 3)
        14
        >>> squares(1)(2)(3)
        14
        >>> squares(1, 2, z=3)
        14
        >>> squares(1, 2)(z=3)
        14
    """
    argnames, vararg, kwarg, defaults = inspect.getargspec(func)
    def replacement(*args, **kw):
        unused = argnames[len(args):]
        for name in kw:
            if name in unused:
                unused.remove(name)
        if unused:
            return partial(replacement, *args, **kw)
        return func(*args, **kw)
    return replacement

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

