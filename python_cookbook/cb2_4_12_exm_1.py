def pairwise_slow(iterable):
    it = iter(iterable)
    while True:
        yield it.next(), it.next()
