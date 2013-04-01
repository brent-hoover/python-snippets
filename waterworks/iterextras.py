"""Some useful iterator functions from py2.4 test_itertools.py plus a
couple added items."""

from itertools import *
__all__ = ['take', 'tabulate', 'iteritems', 'nth', 'all', 'any', 'no',
    'quantify', 'padnone', 'ncycles', 'dotproduct', 'flatten',
    'repeatfunc', 'pairwise', 'tee', 'iunzip', 'batch']

def take(n, seq):
    """Return the first n items in a sequence."""
    return list(islice(seq, n))

def tabulate(function):
    "Return function(0), function(1), ..."
    return imap(function, count())

def iteritems(mapping):
    """Same as dict.iteritems()"""
    return izip(mapping.iterkeys(), mapping.itervalues())

def nth(iterable, n):
    "Returns the nth item"
    return list(islice(iterable, n, n+1))

def all(seq, pred=None):
    "Returns True if pred(x) is true for every element in the iterable"
    for elem in ifilterfalse(pred, seq):
        return False
    return True

def any(seq, pred=None):
    "Returns True if pred(x) is true for at least one element in the iterable"
    for elem in ifilter(pred, seq):
        return True
    return False

def no(seq, pred=None):
    "Returns True if pred(x) is false for every element in the iterable"
    for elem in ifilter(pred, seq):
        return False
    return True

def quantify(seq, pred=None):
    "Count how many times the predicate is true in the sequence"
    return sum(imap(pred, seq))

def padnone(seq):
    "Returns the sequence elements and then returns None indefinitely"
    return chain(seq, repeat(None))

def ncycles(seq, n):
    "Returns the sequence elements n times"
    return chain(*repeat(seq, n))

def dotproduct(vec1, vec2):
    """Return the dot product between two vectors."""
    return sum(imap(operator.mul, vec1, vec2))

def flatten(listOfLists):
    """Flatten a list of lists."""
    return list(chain(*listOfLists))

def repeatfunc(func, times=None, *args):
    "Repeat calls to func with specified arguments."
    "   Example:  repeatfunc(random.random)"
    if times is None:
        return starmap(func, repeat(args))
    else:
        return starmap(func, repeat(args, times))

# attempt to use the real itertools.tee from python2.4
try:
    tee = itertools.tee
except NameError:
    # provide a simple implementation instead
    def tee(iterable, n=2):
        "tee(iterable, n=2) --> tuple of n independent iterators."
        # TODO this is a braindead implementation
        l = list(iterable)
        return [iter(l) for x in range(n)]

# pad option added by dmcc
def pairwise(iterable, pad=False):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    try:
        b.next()
    except StopIteration:
        pass

    if pad:
        return izip(a, padnone(b))
    else:
        return izip(a, b)

# the following are written or added by dmcc -- not in the real iterextras
def batch(iterable, batchsize=2):
    """Yield a list of (up to) batchsize items at a time.  The last
    element will be shorter if there are items left over.
    batch(s, 2) -> [s0,s1], [s2,s3], [s4, s5], ..."""
    current = []
    for item in iterable:
        current.append(item)
        if len(current) == batchsize:
            yield current
            current = []
    if current:
        yield current

def iunzip(iterable, n=None):
    """Takes an iterator that yields n-tuples and returns n iterators
    which index those tuples.  This function is the reverse of izip().
    n is the length of the n-tuple and will be autodetected if not
    specified.  If the iterable contains tuples of differing sizes,
    the behavior is undefined."""
    import operator
    # a braindead implementation for now (since it relies on tee() which is
    # braindead in this module (but not in Python 2.4+))
    iterable = iter(iterable) # ensure we're dealing with an iterable
    if n is None: # check the first element for length
        first = iterable.next()
        n = len(first)
        # now put it back in to iterable is unchanged
        iterable = chain([first], iterable)

    iter_tees = tee(iterable, n)
    selector = lambda index: lambda item: operator.getitem(item, index)
    return [imap(selector(index), iter_tee) 
        for index, iter_tee in izip(count(), iter_tees)]

# from http://groups.google.com/group/comp.lang.python/browse_thread/thread/d364e7b16bf151c7
# by Raymond Hettinger
def split_on(iterable, event, start=True):
    """Split iterable on event boundaries (either start events or stop
    events).

    >>> ' '.join(''.join(x) for x in split_on('X1X23X456X', 'X'.__eq__, True))
    'X1 X23 X456 X'
    >>> ' '.join(''.join(x) for x in split_on('X1X23X456X', 'X'.__eq__, False))
    'X 1X 23X 456X'
    """
    def transition_counter(x, start=start, cnt=[0]):
        before = cnt[0]
        if event(x):
            cnt[0] += 1
        after = cnt[0]
        if start:
            return after
        else:
            return before
    return (g for k, g in groupby(iterable, transition_counter))

def all_pairs(objects):
    """Yields pairs of all objects.  Each pair is only listed once (i.e.
    if we list (a, b) we won't also list (b, a).  Objects in the list
    must implement comparisons for this to work."""
    for obj1 in objects:
        for obj2 in objects:
            if obj2 <= obj1:
                continue
            yield (obj1, obj2)

if __name__ == "__main__":
    test = zip(range(1, 10), range(21, 30), range(81, 90))
    print test
    a, b, c = iunzip(test)
    al = list(a)
    bl = list(b)
    cl = list(c)
    print al
    print bl
    print cl
    recombined = zip(al, bl, cl)
    assert recombined == test
