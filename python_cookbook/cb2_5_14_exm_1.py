def iteritems(self):
        for v, k in self._rating:
            yield k, v
