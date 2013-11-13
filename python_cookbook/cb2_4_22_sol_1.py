def throws(t, f, *a, **k):
    '''Return True iff f(*a, **k) raises an exception whose type is t
      (or, one of the items of _tuple_ t, if t is a tuple).'''
    try:
        f(*a, **k)
    except t:
        return True
    else:
        return False
