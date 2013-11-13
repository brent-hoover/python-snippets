def throws(t, f, *a, **k):
    " Return a pair (True, None) if f(*a, **k) raises exceptions n
      t, else a pair (False, x) where x is the result of f(*a, **k). "
    try:
        return False, f(*a, **k)
    except t:
        return True, None
