class DefaultAlias(object):
    ''' unless explicitly assigned, this attribute aliases to another. '''
    def __init__(self, name):
        self.name = name
    def __get__(self, inst, cls):
        if inst is None:
            # attribute accessed on class, return `self' descriptor
            return self
        return getattr(inst, self.name)
class Alias(DefaultAlias):
    ''' this attribute unconditionally aliases to another. '''
    def __set__(self, inst, value):
        setattr(inst, self.name, value)
    def __delete__(self, inst):
        delattr(inst, self.name)
