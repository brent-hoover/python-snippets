import UserDict
class FifoCache(object, UserDict.DictMixin):
    ''' A mapping that remembers the last `num_entries' items that were set '''
    def __init__(self, num_entries, dct=()):
        self.num_entries = num_entries
        self.dct = dict(dct)
        self.lst = []
    def __repr__(self):
        return '%r(%r,%r)' % (
            self.__class__.__name__, self.num_entries, self.dct)
    def copy(self):
        return self.__class__(self.num_entries, self.dct)
    def keys(self):
        return list(self.lst)
    def __getitem__(self, key):
        return self.dct[key]
    def __setitem__(self, key, value):
        dct = self.dct
        lst = self.lst
        if key in dct:
            lst.remove(key)
        dct[key] = value
        lst.append(key)
        if len(lst) > self.num_entries:
            del dct[lst.pop(0)]
    def __delitem__(self, key):
        self.dct.pop(key)
        self.lst.remove(key)
    # a method explicitly defined only as an optimization
    def __contains__(self, item):
        return item in self.dct
    has_key = __contains__
