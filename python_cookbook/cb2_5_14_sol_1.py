#!/usr/bin/env python
''' An enriched dictionary that holds a mapping from keys to scores '''
from bisect import bisect_left, insort_left
import UserDict
class Ratings(UserDict.DictMixin, dict):
    """ class Ratings is mostly like a dictionary, with extra features: the
        value corresponding to each key is the 'score' for that key, and all
        keys are ranked in terms their scores.  Values must be comparable; keys,
        as well as being hashable, must be comparable if any two keys may ever
        have the same corresponding value (i.e., may be "tied" on score).
        All mapping-like behavior is just as you would expect, such as:
        >>> r = Ratings({"bob": 30, "john": 30})
        >>> len(r)
        2
        >>> r.has_key("paul"), "paul" in r
        (False, False)
        >>> r["john"] = 20
        >>> r.update({"paul": 20, "tom": 10})
        >>> len(r)
        4
        >>> r.has_key("paul"), "paul" in r
        (True, True)
        >>> [r[key] for key in ["bob", "paul", "john", "tom"]]
        [30, 20, 20, 10]
        >>> r.get("nobody"), r.get("nobody", 0)
        (None, 0)
        In addition to the mapping interface, we offer rating-specific
        methods.  r.rating(key) returns the ranking of a key in the
        ratings, with a ranking of 0 meaning the lowest score (when two
        keys have equal scores, the keys themselves are compared, to
        "break the tie", and the lesser key gets a lower ranking):
        >>> [r.rating(key) for key in ["bob", "paul", "john", "tom"]]
        [3, 2, 1, 0]
        getValueByRating(ranking) and getKeyByRating(ranking) return the
        score and key, respectively, for a given ranking index:
        >>> [r.getValueByRating(rating) for rating in range(4)]
        [10, 20, 20, 30]
        >>> [r.getKeyByRating(rating) for rating in range(4)]
        ['tom', 'john', 'paul', 'bob']
        An important feature is that the keys() method returns keys in
        ascending order of ranking, and all other related methods return
        lists or iterators fully consistent with this ordering:
        >>> r.keys()
        ['tom', 'john', 'paul', 'bob']
        >>> [key for key in r]
        ['tom', 'john', 'paul', 'bob']
        >>> [key for key in r.iterkeys()]
        ['tom', 'john', 'paul', 'bob']
        >>> r.values()
        [10, 20, 20, 30]
        >>> [value for value in r.itervalues()]
        [10, 20, 20, 30]
        >>> r.items()
        [('tom', 10), ('john', 20), ('paul', 20), ('bob', 30)]
        >>> [item for item in r.iteritems()]
        [('tom', 10), ('john', 20), ('paul', 20), ('bob', 30)]
        An instance can be modified (adding, changing and deleting
        key-score correspondences), and every method of that instance
        reflects the instance's current state at all times:
        >>> r["tom"] = 100
        >>> r.items()
        [('john', 20), ('paul', 20), ('bob', 30), ('tom', 100)]
        >>> del r["paul"]
        >>> r.items()
        [('john', 20), ('bob', 30), ('tom', 100)]
        >>> r["paul"] = 25
        >>> r.items()
        [('john', 20), ('paul', 25), ('bob', 30), ('tom', 100)]
        >>> r.clear()
        >>> r.items()
        []
        """
    ''' the implementation carefully mixes inheritance and delegation
        to achieve reasonable performance while minimizing boilerplate,
        and, of course, to ensure semantic correctness as above.  All
        mappings' methods not implemented below get inherited, mostly
        from DictMixin, but, crucially!, __getitem__ from dict. '''
    def __init__(self, *args, **kwds):
        ''' This class gets instantiated just like 'dict' '''
        dict.__init__(self, *args, **kwds)
        # self._rating is the crucial auxiliary data structure: a list
        # of all (value, key) pairs, kept in naturally-sorted order
        self._rating = [ (v, k) for k, v in dict.iteritems(self) ]
        self._rating.sort()
    def copy(self):
	''' Provide an identical but independent copy '''
        return Ratings(self)
    def __setitem__(self, k, v):
        ''' besides delegating to dict, we maintain self._rating '''
        if k in self:
            del self._rating[self.rating(k)]
        dict.__setitem__(self, k, v)
        insort_left(self._rating, (v, k))
    def __delitem__(self, k):
        ''' besides delegating to dict, we maintain self._rating '''
        del self._rating[self.rating(k)]
        dict.__delitem__(self, k)
    ''' delegate some methods to dict explicitly to avoid getting
        DictMixin's slower (though correct) implementations instead '''
    __len__ = dict.__len__
    __contains__ = dict.__contains__
    has_key = __contains__
    ''' the key semantic connection between self._rating and the order
        of self.keys() -- DictMixin gives us all other methods 'for
        free', although we could implement them directly for slightly
        better performance. '''
    def __iter__(self):
        for v, k in self._rating:
            yield k
    iterkeys = __iter__
    def keys(self):
        return list(self)
    ''' the three ratings-related methods '''
    def rating(self, key):
        item = self[key], key
        i = bisect_left(self._rating, item)
        if item == self._rating[i]:
            return i
        raise LookupError, "item not found in rating"
    def getValueByRating(self, rating):
        return self._rating[rating][0]
    def getKeyByRating(self, rating):
        return self._rating[rating][1]
def _test():
    ''' we use doctest to test this module, which must be named
        rating.py, by validating all the examples in docstrings. '''
    import doctest, rating
    doctest.testmod(rating)
if __name__ == "__main__":
    _test()
