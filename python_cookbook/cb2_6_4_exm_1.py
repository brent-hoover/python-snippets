import UserDict
from sets import Set
class FullChainmap(Chainmap, UserDict.DictMixin):
    def copy(self):
        return self.__class__(self._mappings)
    def __iter__(self):
        seen = Set()
        for mapping in self._mappings:
            for key in mapping:
                if key not in seen:
                    yield key
                    seen.add(key)
    iterkeys = __iter__
    def keys(self):
        return list(self)
