# support 2.3 as well as 2.4
try: set
except NameError: from sets import Set as set
class ROError(AttributeError): pass
class Readonly: # there IS a reason to NOT subclass object, see Discussion
    mutators = {
        list: set('''__delitem__ __delslice__ __iadd__ __imul__
                 __setitem__ __setslice__ append extend insert
                 pop remove sort'''.split()),
        dict: set('''__delitem__ __setitem__ clear pop popitem
                 setdefault update'''.split()),
        }
    def __init__(self, o):
        object.__setattr__(self, '_o', o)
        object.__setattr__(self, '_no', self.mutators.get(type(o), ()))
    def __setattr__(self, n, v):
        raise ROError, "Can't set attr %r on RO object" % n
    def __delattr__(self, n):
        raise ROError, "Can't del attr %r from RO object" % n
    def __getattr__(self, n):
        if n in self._no:
            raise ROError, "Can't get attr %r from RO object" % n
        return getattr(self._o, n)
