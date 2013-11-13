import itertools
def tee(iterable):
    def yield_with_cache(next, cache={}):
        pop = cache.pop
        for i in itertools.count():
            try:
                yield pop(i)
            except KeyError:
                cache[i] = next()
                yield cache[i]
    it = iter(iterable)
    return yield_with_cache(it.next), yield_with_cache(it.next)
