class list_with_aux_dict(list):
    def __init__(self, iterable=()):
        list.__init__(self, iterable)
        self._dict_ok = False
    def _rebuild_dict(self):
	self._dict = {}
	for i, item in enumerate(self):
	    if item not in self._dict:
                self._dict[item] = i
	self._dict_ok = True
    def __contains__(self, item):
        if not self._dict_ok:
	    self._rebuild_dict()
        return item in self._dict
    def index(self, item):
        if not self._dict_ok:
	    self._rebuild_dict()
        try: return self._dict[item]
	except KeyError: raise ValueError
def _wrapMutatorMethod(methname):
    _method = getattr(list, methname)
    def wrapper(self, *args):
        # Reset 'dictionary OK' flag, then delegate to the real mutator method
        self._dict_ok = False
        return _method(self, *args)
    # in Python 2.4, only: wrapper.__name__ = _method.__name__
    setattr(list_with_aux_dict, methname, wrapper)
for meth in 'setitem delitem setslice delslice iadd'.split():
    _wrapMutatorMethod('__%s__' % meth)
for meth in 'append insert pop remove extend'.split():
    _wrapMutatorMethod(meth)
del _wrapMethod               # remove auxiliary function, not needed any more
