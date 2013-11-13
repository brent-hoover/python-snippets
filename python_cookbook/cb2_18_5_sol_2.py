def memoize(fn):
    memo = {}
    def memoizer(*param_tuple, **kwds_dict):
        # can't memoize if there are any named arguments
        if kwds_dict:
            return fn(*param_tuple, **kwds_dict)
        try:
            # try using the memo dict, or else update it
            try:
                return memo[param_tuple]
            except KeyError:
                memo[param_tuple] = result = fn(*param_tuple)
                return result
        except TypeError:
            # some mutable arguments, bypass memoizing
            return fn(*param_tuple)
    # 2.4 only: memoizer.__name__ = fn.__name__
    return memoizer
