if n is None:
            result = self._cache.pop(0)
        else:
            result, self_cache = self._cache[:n], self._cache[n:]
