"""Collection of functions and classes for working on dictionaries."""

try:
    from collections import defaultdict
    _py25_or_better = True
except ImportError:
    _py25_or_better = False

# TODO this will convert to a collections.Counter at some point...
class CounterDict(dict):
    """Simple subclass of a dictionary to help count items:
    
    >>> c = CounterDict()
    >>> c.count('a', 'sequence', 'of', 'things', 'to', 'count')
    >>> c
    {'a': 1, 'count': 1, 'sequence': 1, 'of': 1, 'to': 1, 'things': 1}
    >>> c.count('more', 'things')
    >>> c
    {'a': 1, 'count': 1, 'sequence': 1, 'of': 1, 'to': 1, 'things': 2, 'more': 1}
    >>> c.count('justonething')
    >>> c
    {'a': 1, 'count': 1, 'sequence': 1, 'of': 1, 'to': 1, 'justonething': 1, 'things': 2, 'more': 1}
    >>> c.scale(5)                                                                  >>> c
    {'a': 5, 'count': 5, 'sequence': 5, 'of': 5, 'to': 5, 'justonething': 5, 'things': 10, 'more': 5}
    >>> c2 = CounterDict()
    >>> c2.count_many_times('a', 3)
    >>> c2
    {'a': 3}
    >>> c.merge(c2)
    >>> c
    {'a': 8, 'count': 5, 'sequence': 5, 'of': 5, 'to': 5, 'justonething': 5, 'things': 10, 'more': 5}
    """
    def count(self, *keys):
        "Count each item in the sequence 'keys' (which could be a single item)"
        for key in keys:
            self.setdefault(key, 0)
            self[key] += 1
    def count_many_times(self, key, count):
        "Count an item 'count' times."
        self.setdefault(key, 0)
        self[key] += count
    def merge(self, *otherdicts):
        """Merge (add) the counts from other dictionaries into this one."""
        for otherdict in otherdicts:
            for key, value in otherdict.items():
                self.setdefault(key, 0)
                self[key] += value
    def __add__(self, other):
        """Non-destructive add, returns a new CounterDict"""
        new_counterdict = self.__class__()
        new_counterdict.merge(self)
        new_counterdict.merge(other)
        return new_counterdict
    def __iadd__(self, other):
        """Destructive add, returns None"""
        self.merge(other)
    def scale(self, multiplier):
        """Multiplies all counts by multiplier."""
        for key in list(self.keys()):
            self[key] *= multiplier
    def most_common(self, n=None):
        """Returns a list of the n most common elements and their counts.
        Returns all elements and counts if n is None.
        (see collections.Counter.most_common)"""
        items = sorted(self.items(), key=lambda (item, count): (-count, item))
        if n is not None:
            return items[:n]
        else:
            return items
    def entropy(self):
        from Probably import entropy_of_multinomial
        return entropy_of_multinomial(self.values())

if _py25_or_better:
# these doctests probably don't work due to dictionary random shuffling
    class TwoLevelCounterDict(defaultdict):
        """Dictionary of CounterDict objects.

        >>> t = TwoLevelCounterDict()
        >>> t['outer1'].count('inner1', 'inner2')
        >>> print t
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer1': {'inner2': 1, 'inner1': 1}})
        >>> t['outer2'].count('inner1', 'inner3', 'inner4')
        >>> print t
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer1': {'inner2': 1, 'inner1': 1}, 'outer2': {'inner4': 1, 'inner3': 1, 'inner1': 1}})
        >>> print t['outer1']
        {'inner2': 1, 'inner1': 1}
        >>> t.scale(5)
        >>> print t
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer1': {'inner2': 5, 'inner1': 5}, 'outer2': {'inner4': 5, 'inner3': 5, 'inner1': 5}})
        >>> t['outer1'].count('inner1', 'inner2')
        >>> t['outer2'].count('inner1', 'inner3', 'inner4')
        >>> t.scale(5)
        >>> t
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer1': {'inner2': 5, 'inner1': 5}, 'outer2': {'inner4': 5, 'inner3': 5, 'inner1': 5}})
        >>> t2 = TwoLevelCounterDict()
        >>> t2['outer2'].count('inner3')
        >>> t2['outer3'].count('inner10')
        >>> t2['outer4'].count('inner1', 'inner2')
        >>> t2['outer4'].count_many_times('inner7', 7)
        >>> print t2
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer4': {'inner7': 7, 'inner2': 1, 'inner1': 1}, 'outer3': {'inner10': 1}, 'outer2': {'inner3': 1}})
        >>> t2.merge(t)
        >>> sorted(t2.keys())
        ['outer1', 'outer2', 'outer3', 'outer4']
        >>> print t2
        defaultdict(<class 'waterworks.Dictionaries.CounterDict'>, {'outer4': {'inner7': 7, 'inner2': 1, 'inner1': 1}, 'outer1': {'inner2': 5, 'inner1': 5}, 'outer3': {'inner10': 1}, 'outer2': {'inner4': 5, 'inner3': 6, 'inner1': 5}})
        """
        def __init__(self, *args):
            """Doesn't actually take any arguments (the *args is to get
            around a pickling problem."""
            defaultdict.__init__(self, CounterDict)
        def scale(self, multiplier):
            """Multiply all inner-dictionaries by multiplier (in place)"""
            for d in self.values():
                d.scale(multiplier)
        def merge(self, *others):
            all_keys = set(self.keys())
            for other in others:
                all_keys.update(other.keys())
                for key in all_keys:
                    self[key].merge(other[key])

def dictadd(d1, d2):
    """Add the numeric values of values in two dictionaries together in
    a functional fashion (d1 and d2 are not modified)."""
    # we're going to clone d1, so we'll reverse our arguments if d2 is the
    # smaller one
    if len(d2) < len(d1):
        d1, d2 = d2, d1
    d1 = dict(d1) # clone d1
    return dictiadd(d1, d2)

def dictiadd(d1, d2):
    """Add the numeric values of values in two dictionaries together,
    modifying the first argument in place. (Called iadd to be like
    Python's __iadd__ which is the method that does incremental
    addition)."""
    for k, v in d2.items():
        d1.setdefault(k, 0)
        d1[k] += v
    return d1

def dictmultiply(d, multiplier, dict=dict):
    """Returns a dictionary with all values multiplied by multiplier."""
    return dict((key, value * multiplier)
        for key, value in d.items())

def dictmax(d1, d2):
    """Returns a new dictionary with the union of the keys found in d1 and d2
    and the values the maximum value."""
    new_dict = {}
    for key, value1 in d1.items():
        if key in d2:
            new_dict[key] = max(value1, d2[key])
        else:
            new_dict[key] = value1

    # now do keys only in d2
    for key, value2 in d2.items():
        if key not in d1:
            new_dict[key] = value2
    return new_dict

def countdict_to_pairs(counts, limit=None):
    """Convert a dictionary from { anything : counts } to a list of at
    most 'limit' pairs (or all if limit is None), sorted from highest
    count to lowest count."""
    pairs = [(count, x) for (x, count) in counts.items() if count]
    pairs.sort()
    pairs.reverse() # sort from high to low
    if limit is not None:
        pairs = pairs[:limit]

    return pairs

def dict_subset(d, dkeys, default=0):
    """Subset of dictionary d: only the keys in dkeys.  If you plan on omitting
    keys, make sure you like the default."""
    newd = {} # dirty variables!
    for k in dkeys:
        newd[k] = d.get(k, default)
    return newd
