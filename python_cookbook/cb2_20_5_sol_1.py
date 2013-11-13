class CommonProperty(object):
    def __init__(self, realname, fget=getattr, fset=setattr, fdel=delattr,
                 doc=None):
        self.realname = realname
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc or ""
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError, "can't get attribute"
        return self.fget(obj, self.realname)
    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError, "can't set attribute"
        self.fset(obj, self.realname, value)
    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError, "can't delete attribute"
        self.fdel(obj, self.realname, value)
