class EnumException(Exception):
    pass
class Enumeration(object):
    def __init__(self, name, enumList, valuesAreUnique=True):
        self.__doc__ = name
        self.lookup = lookup = {}
        self.reverseLookup = reverseLookup = {}
        i = 0
        for x in enumList:
            if type(x) is tuple:
                try:
                    x, i = x
                except ValueError:
                    raise EnumException, "tuple doesn't have 2 items: %r" % (x,)
            if type(x) is not str:
                raise EnumException, "enum name is not a string: %r" % (x,)
            if type(i) is not int:
                raise EnumException, "enum value is not an integer: %r" % (i,)
            if x in lookup:
                raise EnumException, "enum name is not unique: %r" % (x,)
            if valuesAreUnique and i in reverseLookup:
                raise EnumException, "enum value %r not unique for %r" % (i, x)
            lookup[x] = i
            reverseLookup[i] = x
            i = i + 1
    def __getattr__(self, attr):
        try: return self.lookup[attr]
        except KeyError: raise AttributeError, attr
    def whatis(self, value):
        return self.reverseLookup[value]
