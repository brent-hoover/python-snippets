def compose(f, g, *args_for_f, **kwargs_for_f):
    ''' compose functions.  compose(f, g, x)(y) = f(g(y), x)) '''
    def fg(*args_for_g, **kwargs_for_g):
        return f(g(*args_for_g, **kwargs_for_g), *args_for_f, **kwargs_for_f)
    return fg
def mcompose(f, g, *args_for_f, **kwargs_for_f):
    ''' compose functions.  mcompose(f, g, x)(y) = f(*g(y), x)) '''
    def fg(*args_for_g, **kwargs_for_g):
        mid = g(*args_for_g, **kwargs_for_g)
        if not isinstance(mid, tuple):
            mid = (mid,)
        return f(*(mid+args_for_f), **kwargs_for_f)
    return fg
