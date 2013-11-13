def memoize(fn):
    memo = {}
    def memoizer(*param_tuple, **kwds_dict):
        if kwds_dict:
            memoizer.namedargs += 1
            return fn(*param_tuple, **kwds_dict)
        try:
            memoizer.cacheable += 1
            try:
                return memo[param_tuple]
            except KeyError:
                memoizer.misses += 1
                memo[param_tuple] = result = fn(*param_tuple)
                return result
        except TypeError:
            memoizer.cacheable -= 1
            memoizer.noncacheable += 1
            return fn(*param_tuple)
    memoizer.namedargs = memoizer.cacheable = memoizer.noncacheable = 0
    memoizer.misses = 0
    return memoizer
