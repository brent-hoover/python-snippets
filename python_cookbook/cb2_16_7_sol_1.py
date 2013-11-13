class peek_ahead(object):
    sentinel = object()
    def __init__(self, it):
        self._nit = iter(it).next
        self.preview = None
        self._step()
    def __iter__(self):
        return self
    def next(self):
        result = self._step()
        if result is self.sentinel: raise StopIteration
        else: return result
    def _step(self):
        result = self.preview
        try: self.preview = self._nit()
        except StopIteration: self.preview = self.sentinel
        return result
