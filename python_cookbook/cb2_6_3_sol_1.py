def no_new_attributes(wrapped_setattr):
    """ raise an error on attempts to add a new attribute, while
        allowing existing attributes to be set to new values.
    """
    def __setattr__(self, name, value):
        if hasattr(self, name):    # not a new attribute, allow setting
            wrapped_setattr(self, name, value)
        else:                      # a new attribute, forbid adding it
            raise AttributeError("can't add attribute %r to %s" % (name, self))
    return __setattr__
class NoNewAttrs(object):
    """ subclasses of NoNewAttrs inhibit addition of new attributes, while
        allowing existing attributed to be set to new values.
    """
    # block the addition new attributes to instances of this class
    __setattr__ = no_new_attributes(object.__setattr__)
    class __metaclass__(type):
        " simple custom metaclass to block adding new attributes to this class "
        __setattr__ = no_new_attributes(type.__setattr__)
