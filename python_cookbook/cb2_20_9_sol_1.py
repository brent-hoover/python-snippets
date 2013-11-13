class IMinimalMapping(object):
    def __getitem__(self, key): pass
    def __setitem__(self, key, value): pass
    def __delitem__(self, key): pass
    def __contains__(self, key): pass
import UserDict
class IFullMapping(IMinimalMapping, UserDict.DictMixin):
    def keys(self): pass
class IMinimalSequence(object):
    def __len__(self): pass
    def __getitem__(self, index): pass
class ICallable(object):
    def __call__(self, *args): pass
