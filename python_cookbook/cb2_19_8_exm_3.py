import itertools
def par_two(a, b, padding_item=None):
    a, b = iter(a), iter(b)
    # first, deal with both iterables via izip until one is exhausted:
    for x in itertools.izip(a, b):
        yield x
    # only one of the following two loops, at most, will execute, since
    # either a or b (or both!) are exhausted at this point:
    for x in a:
        yield x, padding_item
    for x in b:
        yield padding_item, x
