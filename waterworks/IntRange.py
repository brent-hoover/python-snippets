"""Integer Range Parser and Generator"""
# TODO docs coming soon, for now we have examples
import re
from waterworks.Strings import multisplit

def parse(string_to_parse, range_markers=(r'-', r'\.\.'), 
          range_delimiters=(',', ' ')):
    """Example:

    >>> print parse("1-7, 20-25, 19, 12, 109-111")
    [1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 24, 25, 19, 12, 109, 110, 111]
    >>> print parse("1-7, 20..25, 19, 12, 109-111")
    [1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 24, 25, 19, 12, 109, 110, 111]
    """
    range_segments = multisplit(string_to_parse, range_delimiters)
    ints = []
    for segment in range_segments:
        try:
            start, end = multisplit(segment, range_markers)
            start = int(start)
            end = int(end)
            ints.extend(range(start, end + 1))
        except ValueError:
            ints.append(int(segment))

    return ints

# TODO: one can insert a range that is enclosed by an outer range.
# this shouldn't be possible -- we should use an integer tree
class Rangifier:
    """Example:

    >>> print Rangifier([1, 5, 6, 2, 3])
    1-3, 5-6
    >>> print Rangifier([1, 2, 3, 4, 6])
    1-4, 6
    >>> print Rangifier([6, 4, 3, 2, 1])
    1-4, 6
    >>> print Rangifier([1, 2, 3, 6, 5, 4])
    1-6
    >>> print Rangifier("1-6")
    1-6
    """
    def __init__(self, seq):
        self.starts = {} # start : (start, end)
        self.ends = {}   # end : (start, end)

        if isinstance(seq, basestring):
            seq = parse(seq)

        for elt in seq:
            elt = int(elt)
            self.add(elt, elt)
    def __str__(self):
        pieces = []
        for range in self.get_ranges():
            start, end = range
            if start == end:
                pieces.append(str(start))
            else:
                pieces.append("%s-%s" % range)
        return ', '.join(pieces)
    def __iter__(self):
        for (start, end) in self.get_ranges():
            for x in range(start, end + 1):
                yield x
    def add(self, newstart, newend):
        newrange = (newstart, newend)
        oldrange = None
        if newstart - 1 in self.ends:
            oldrange = self.ends[newstart - 1]
            newrange = self._merge_ranges((newstart - 1, newend), oldrange)
        elif newend + 1 in self.starts:
            oldrange = self.starts[newend + 1]
            newrange = self._merge_ranges((newstart, newend + 1), oldrange)
        if oldrange:
            self._forget_range(oldrange)
            # try to do further merges
            self.add(*newrange)
        else:
            self._store_range(newrange)
    def _merge_ranges(self, range1, range2):
        start1, end1 = range1
        start2, end2 = range2

        if start1 == end2:
            return (start2, end1)
        elif start2 == end1:
            return (start1, end2)
        
        raise IndexError(range1, range2)
    def _store_range(self, range):
        start, end = range
        self.starts[start] = range
        self.ends[end] = range
    def _forget_range(self, (start, end)):
        del self.starts[start]
        del self.ends[end]
    def get_ranges(self):
        ranges = self.ends.values()
        ranges.sort()
        return ranges

def test_module():
    import doctest, IntRange # !!!
    return doctest.testmod(IntRange)

if __name__ == "__main__":
    # import sys
    # print parse(sys.argv[1])

    print "testing"
    test_module()
    print list(Rangifier([1,2,3,4]))
