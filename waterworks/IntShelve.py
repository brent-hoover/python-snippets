"""Just like shelve, but keys are always integers instead of strings."""
import shelve, anydbm, os

# this module is in the middle of (stalled) refactoring.
# the goal is to ensure that IntShelve is close enough to IW.
# also, WriteOnDemandShelve should probably its own module.

class IntShelve:
    """Interface to shelve where keys are always integers."""
    def __init__(self, filename):
        self._filename = filename
        # open in read mode for now, but switch to write on the first write
        self._write_mode = False
        if os.path.exists(filename):
            mode = 'r' # "read" = read, don't create
        else:
            mode = 'n' # "new" = read-create
        self._shelve = shelve.open(filename, flag=mode)
    def _ensure_write_mode(self):
        if not self._write_mode:
            # we reopen in read-write mode
            self._shelve = shelve.open(self._filename, flag='c')
            self._write_mode = True
    # dispatch everything we don't implement to _shelve
    def __getattr__(self, attr):
        return getattr(self._shelve, attr)
    
    # these methods are nearly the same, but we str()ify int keys
    def __getitem__(self, key):
        return self._shelve[str(key)]
    def __setitem__(self, key, value):
        self._ensure_write_mode()
        self._shelve[str(key)] = value
    def __delitem__(self, key):
        self._ensure_write_mode()
        del self._shelve[str(key)]
    def update(self, new_dict):
        self._ensure_write_mode()
        new_dict_str = dict([(str(k), v) for k, v in new_dict.items()])
        self._shelve.update(new_dict_str)
    def pop(self, key, default=None):
        self._ensure_write_mode()
        self._shelve.pop(str(key))
    def popitem(self):
        self._ensure_write_mode()
        k, v = self._shelve.popitem()
        return (int(k), v)
    def setdefault(self, key, default):
        if key not in self:
            self._ensure_write_mode()
            self[key] = default
    def clear(self):
        self._ensure_write_mode()
        self._shelve.clear()
    def __iter__(self):
        for key in self._shelve.keys():
            yield int(key)
    def keys(self):
        return [key for key in self]
    def get(self, key, default=None):
        return self._shelve.get(str(key), default)
    def items(self):
        return [(int(k), v) for k, v in self._shelve.items()]
    def iteritems(self):
        for k, v in self._shelve.items():
            yield (int(k), v)

# TODO: make IntShelve a child of this
import UserDict
class WriteOnDemandShelve(UserDict.DictMixin):
    def __init__(self, filename):
        self._filename = filename
        # open in read mode for now, but switch to write on the first write
        self._write_mode = False
        if os.path.exists(filename):
            mode = 'r' # "read" = read, don't create
        else:
            mode = 'n' # "new" = read only, create
        self._shelve = shelve.open(filename, flag=mode)

    # this methods is nearly the same, but we str()ify keys
    def __getitem__(self, key):
        return self._shelve[str(key)]
    def keys(self):
        return self._shelve.keys()

    # these methods require working in read-write mode
    def _ensure_write_mode(self):
        if not self._write_mode:
            # we reopen in read-write mode
            self._shelve = shelve.open(self._filename, flag='c')
            self._write_mode = True
    def __setitem__(self, key, value):
        self._ensure_write_mode()
        self._shelve[str(key)] = value
    def __delitem__(self, key):
        if type(key) is slice:
            self.__delslice__(key.start, key.stop, key.step)
        else:
            self._ensure_write_mode()
            del self._shelve[str(key)]
    def __delslice__(self, start, stop, step=None):
        raise TypeError("Deleting slices not supported!")

# this will become IntShelve
class IW(WriteOnDemandShelve):
    # def __getitem__
    def __iter__(self):
        for key in WriteOnDemandShelve.keys(self):
            yield int(key)
    def get(self, key, default=None):
        if default is not None:
            default = str(default)
        return WriteOnDemandShelve.get(self, str(key), default)
    def items(self):
        return [(int(k), v) for k, v in WriteOnDemandShelve.items(self)]
    def iteritems(self):
        for k, v in WriteOnDemandShelve.iteritems(self):
            yield (int(k), v)
    def __delslice__(self, start, stop, step=None):
        if step == None:
            step = 1
        keys = range(start, stop, step)
        for key in keys:
            del self[key]
