"""
Class/metaclass version of property.

The replacement 'property' class acts much like the original -- you
can call it with four optional arguments (get/set/del/doc), and it
returns a descriptor which will use those arguments.  However, you can
also subclass it, defining the optional member functions
fget/fset/fdel and it uses those to create a descriptor.
"""

real_property = property

class property_meta(type):

    def __new__(meta, class_name, bases, new_attrs):
        if bases == (object,):
            # The property class itself
            return type.__new__(meta, class_name, bases, new_attrs)
        fget = new_attrs.get('fget')
        fset = new_attrs.get('fset')
        fdel = new_attrs.get('fdel')
        fdoc = new_attrs.get('__doc__')
        return real_property(fget, fset, fdel, fdoc)

class property(object):

    __metaclass__ = property_meta

    def __new__(cls, fget=None, fset=None, fdel=None, fdoc=None):
        if fdoc is None and fget is not None:
            fdoc = fget.__doc__
        return real_property(fget, fset, fdel, fdoc)

__test__ = {
    'normal': r"""
    >>> class X(object):
    ...     class double(property):
    ...         'Double the value of obj.value'
    ...         def fget(self):
    ...             return self.value * 2
    ...         def fset(self, value):
    ...             self.value = value / 2
    ...         def fdel(self):
    ...             del self.value
    ...     def _get_half(self):
    ...         return self.value / 2
    ...     half = property(_get_half)
    >>> x = X()
    >>> x.value = 1
    >>> x.double
    2
    >>> x.double = 4
    >>> x.double
    4
    >>> x.value
    2
    >>> del x.double
    >>> x.value
    Traceback (most recent call last):
    AttributeError: 'X' object has no attribute 'value'
    >>> x.value = 100
    >>> x.half
    50
    """}

if __name__ == '__main__':
    import doctest
    doctest.testmod()

