import collections
def tee_just_an_example(iterable):
    def yield_with_cache(it, cache=collections.deque):
        while True:
            if cache:
                yield cache.popleft()
            else:
                result = it.next()
                cache.append(result)
                yield result
    it = iter(iterable)
    return yield_with_cache(it), yield_with_cache(it)
