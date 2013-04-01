"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52201
Title: Memoizing (cacheing) function return values
Submitter: Paul Moore
Last Updated: 2001/10/16
Version no: 1.1

Description:
For functions which are called often, particulary recursive functions
or functions which are intensive to calculate, memoizing (cacheing)
the return values can dramatically improve performance.
"""

class Memoize:
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]
    def clear(self):
        """Forget all memoized results."""
        self.memo.clear()

# this came from a different recipe
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/325205
# TODO: incorporate more of their code (ImmutableDict, e.g.)
import types
def cachedmethod(function):
    return types.MethodType(Memoize(function), None)
