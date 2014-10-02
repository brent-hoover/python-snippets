# a decorator receives the method it's wrapping as a variable 'f'
def increment(f):
    # we use arbitrary args and keywords to
    # ensure we grab all the input arguments.
    def wrapped_f(*args, **kw):
        # note we call f against the variables passed into the wrapper,
        # and cast the result to an int and increment .
        return int(f(*args, **kw)) + 1
    return wrapped_f  # the wrapped function gets returned.


@increment
def plus(a, b):
    return a + b

if __name__ == '__main__':
    result = plus(4, 6)
    print(result)
