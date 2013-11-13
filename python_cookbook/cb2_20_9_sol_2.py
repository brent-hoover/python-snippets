# ensure we use the best available 'set' type with name 'set'
try:
    set
except NameError:
    from sets import Set as set
# a custom exception class that we raise to signal violations
class InterfaceOmission(TypeError):
    pass
class MetaInterfaceChecker(type):
    ''' the interface-checking custom metaclass '''
    def __init__(cls, classname, bases, classdict):
        super(MetaInterfaceChecker, cls).__init__(classname, bases, classdict)
        cls_defines = set(dir(cls))
        for interface in cls.__implements__:
            itf_requires = set(dir(interface))
            if not itf_requires.issubset(cls_defines):
                raise InterfaceOmission, list(itf_requires - cls_defines)
