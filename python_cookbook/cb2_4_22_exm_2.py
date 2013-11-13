def returns(t, f, *a, **k):
    " Return [f(*a, **k)] normally, [] if that raises an exception in t. "
    try:
        return [ f(*a, **k) ]
    except t:
        return [ ]
