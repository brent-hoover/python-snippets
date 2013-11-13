import warnings
class OldAlias(Alias):
    def _warn(self):
        warnings.warn('use %r, not %r' % (self.name, self.oldname),
                      DeprecationWarning, stacklevel=3)
    def __init__(self, name, oldname):
        super(OldAlias, self).__init__(name)
        self.oldname = oldname
    def __get__(self, inst, cls):
        self._warn()
        return super(OldAlias, self).__get__(inst, cls)
    def __set__(self, inst, value):
        self._warn()
        return super(OldAlias, self).__set__(inst, value)
    def __delete__(self, inst):
        self._warn()
        return super(OldAlias, self).__delete__(inst)
