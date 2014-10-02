def minimum_x(x):
    '''
    Write a function decorator that takes an argument, and returns a decorator
    that can be used to decorate a function, which verifies that the first
    argument to a decorated function is at least the given value, raising a
    ValueError on failure.
    >>> @minimum_x(6)
    ... def test(arg):
    ...   print arg
    ...
    >>> test(6)
    6
    >>> test(5) # raises ValueError
    '''
    def minimum(mnm):
        def decorator(func):
            def wrapper(val):
                if val < mnm:
                    raise ValueError()
                result = func(val)
                return result
            return wrapper
        return decorator
