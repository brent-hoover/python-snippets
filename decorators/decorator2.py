
class memoize(object):
    def __init__(self, max):
        self.max = max

    def __call__(self, func):
        return decorator(self.check_cache, func)

    def check_cache(self, func, *args):
        if not hasattr(func, 'results'):
            func.results = dict()
        if args not in func.results:
            func.results[args] = func(*args)
        return func.results[args]



@memoize
def find_user(user_id):
    #query database and find user object
    return User.m_get(_id=user_id)
