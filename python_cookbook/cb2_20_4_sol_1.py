class CachedAttribute(object):
    ''' Computes attribute value and caches it in the instance. '''
    def __init__(self, method, name=None):
        # record the unbound-method and the name
        self.method = method
        self.name = name or method.__name__
    def __get__(self, inst, cls):
        if inst is None:
            # instance attribute accessed on class, return self
            return self
        # compute, cache and return the instance's attribute value
        result = self.method(inst)
        setattr(inst, self.name, result)
        return result
class CachedClassAttribute(CachedAttribute):
    ''' Computes attribute value and caches it in the class. '''
    def __get__(self, inst, cls):
        # just delegate to CachedAttribute, with 'cls' as ``instance''
        return super(CachedClassAttribute, self).__get__(cls, cls)
