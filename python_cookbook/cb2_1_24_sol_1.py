class iStr(str):
    """
    Case insensitive string class.
    Behaves just like str, except that all comparisons and lookups
    are case insensitive.
    """
    def __init__(self, *args):
        self._lowered = str.lower(self)
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))
    def __hash__(self):
        return hash(self._lowered)
    def lower(self):
        return self._lowered
def _make_case_insensitive(name):
    ''' wrap one method of str into an iStr one, case-insensitive '''
    str_meth = getattr(str, name)
    def x(self, other, *args):
        ''' try lowercasing 'other', which is typically a string, but
            be prepared to use it as-is if lowering gives problems,
            since strings CAN be correctly compared with non-strings.
        '''
        try: other = other.lower()
        except (TypeError, AttributeError, ValueError): pass
        return str_meth(self._lowered, other, *args)
    # in Python 2.4, only, add the statement: x.func_name = name
    setattr(iStr, name, x)
# apply the _make_case_insensitive function to specified methods 
for name in 'eq lt le gt gt ne cmp contains'.split():
    _make_case_insensitive('__%s__' % name)
for name in 'count endswith find index rfind rindex startswith'.split():
    _make_case_insensitive(name)
# note that we don't modify methods 'replace', 'split', 'strip', ...
# of course, you can add modifications to them, too, if you prefer that.
del _make_case_insensitive    # remove helper function, not needed any more
