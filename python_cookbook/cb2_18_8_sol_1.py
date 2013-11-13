from operator import itemgetter
from heapq import nlargest
class bag(object):
    def __init__(self, iterable=()):
        # start empty, then add the `iterable' if any
        self._data = {}
        self.update(iterable)
    def update(self, iterable):
        # update from an element->count mapping, or from any iterable
        if isinstance(iterable, dict):
            for elem, n in iterable.iteritems():
                self[elem] += n
        else:
            for elem in iterable:
                self[elem] += 1 
    def __contains__(self, elem):
        # delegate membership test
        return elem in self._data
    def __getitem__(self, elem):
        # default all missing items to a count of 0
        return self._data.get(elem, 0)
    def __setitem__(self, elem, n):
        # setting an item to a count of 0 removes the item
        self._data[elem] = n
        if n == 0:
            del self._data[elem]
    def __delitem__(self, elem):
        # delegate to __setitem__ to allow deleting missing items
        self[elem] = 0
    def __len__(self):
        # length is computed on-the-fly
        return sum(self._data.itervalues())
    def __nonzero__(self):
        # avoid truth tests using __len__, as it's relatively slow
        return bool(self._data)
    def __eq__(self, other):
        # a bag can only equal another bag
        if not isinstance(other, bag):
            return False
        return self._data == other._data
    def __ne__(self, other):
        # a bag always differs from any non-bag
        return not (self == other)
    def __hash__(self):
        # a bag can't be a dict key nor an element in a set
        raise TypeError
    def __repr__(self):
        # typical string-representation
        return '%s(%r)' % (self.__class__.__name__, self._data)
    def copy(self):
        # make and return a shallow copy
        return self.__class__(self._data)
    __copy__ = copy # For the copy module
    def clear(self):
        # remove all items
        self._data.clear()
    def __iter__(self):
        # yield each element the # of times given by its count
        for elem, cnt in self._data.iteritems():
            for i in xrange(cnt):
                yield elem
    def iterunique(self):
        # yield each element only once
        return self._data.iterkeys()
    def itercounts(self):
        # yield element-count pairs
        return self._data.iteritems()     
    def mostcommon(self, n=None):
        # return the n (default: all) most common elements, each as an
        # element-count pair, as a list sorted by descending counts
        if n is None:
            return sorted(self.itercounts(), key=itemgetter(1), reverse=True)
        it = enumerate(self.itercounts())
        nl = nlargest(n, ((cnt, i, elem) for (i, (elem, cnt)) in it))
        return [(elem, cnt) for cnt, i, elem in nl]
