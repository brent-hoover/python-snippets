def peel(iterable, arg_cnt=1):
    """ Yield each of the first arg_cnt items of the iterable, then
        finally an iterator for the rest of the iterable. """
    iterator = iter(iterable)
    for num in xrange(arg_cnt):
        yield iterator.next()
    yield iterator
if __name__ == '__main__':
    t5 = range(1, 6)
    a, b, c = peel(t5, 2)
    print a, b, list(c)
# emits: 1 2 [3, 4, 5]
