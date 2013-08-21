class DictDoc(object):
    """ Adds a mapping interface to a document.  Supports ``__getitem__`` and
        ``__contains__``.  Both methods will only retrieve values assigned to
        a field, not methods or other attributes.
    """
    def __getitem__(self, name):
        """ Gets the field ``name`` from the document """
        fields = self.get_fields()
        if name in fields:
            return getattr(self, name)
        raise KeyError(name)

    def __setitem__(self, name, value):
        """ Sets the field ``name`` on the document """
        setattr(self, name, value)

    def setdefault(self, name, value):
        """ if the ``name`` is set, return its value.  Otherwse set ``name`` to
            ``value`` and return ``value``"""
        if name in self:
            return self[name]
        self[name] = value
        return self[name]

    def __contains__(self, name):
        """ Return whether a field is present.  Fails if ``name`` is not a
            field or ``name`` is not set on the document or if ``name`` was
            not a field retrieved from the database
        """
        try:
            self[name]
        except FieldNotRetrieved:
            return False
        except AttributeError:
            return False
        except KeyError:
            return False
        return True
