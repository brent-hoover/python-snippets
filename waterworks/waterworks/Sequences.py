"""Collection of functions and classes for working on sequences (lists,
tuples, etc.)."""

# from http://www.hetland.org/python/distance.py
def edit_distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n
        
    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * m
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]

def power_set(seq):
    """Returns the power set of an (indexable) sequence."""
    if seq:
        for s in power_set(seq[1:]):
            yield s
        for s in (seq[:1] + y for y in power_set(seq[1:])):
            yield s
    else:
        yield seq

# TODO the following two functions should be more similar
# also, they should work the same way as the real max and min in terms
# of arguments
def maxwithundef(*args, **kw):
    """Optional keyword argument: undef.  Use this to specify an undefined 
    value.  Any argument with that value will be dropped.  If there are no
    valid arguments, undef is returned.  Default is None."""
    undef = kw.get('undef', None)
    args = [arg for arg in args if arg != undef]
    if not args:
        return undef
    elif len(args) == 1:
        return args[0]
    else:
        return max(*args)

def minwithundef(*args, **kw):
    """Optional keyword argument: undef.  Use this to specify an undefined 
    value.  Any argument with that value will be dropped.  If there are no
    valid arguments, undef is returned.  Default is None."""
    undef = kw.get('undef', None)
    args = [arg for arg in args if arg != undef]
    if not args:
        return undef
    elif len(args) == 1:
        return args[0]
    else:
        return min(*args)

def find_indices_of_unique_items(seq, sorted=True):
    """Return a pair of a list of unique indices and a hash table mapping
    nonunique indices to the first instance of it.  Unclear?  See this
    example:
    
    >>> x = [101, 102, 103, 101, 104, 106, 107, 102, 108, 109]
    >>> find_indices_of_unique_items(x)
    ([0, 1, 2, 4, 5, 6, 8, 9], {3: 0, 7: 1})"""
    vals = {} # item : index
    nonunique = {} # index : originalindex

    for index, elt in enumerate(seq):
        if elt in vals:
            originalindex = vals[elt]
            nonunique[index] = originalindex
        else:
            vals[elt] = index

    keys = vals.values()
    if sorted:
        keys.sort()

    return keys, nonunique

def separate_by_pred(pred, iterable, key=None):
    """Splits an iterable by a predicate into two lists depending on the
    predicate's truth value.  The first list is where the predicate holds.
    The second list is where it does not.  Optionally takes a key which
    can transform each element in the iterable."""
    yes = []
    no = []
    for elt in iterable:
        if pred(elt):
            lst = yes
        else:
            lst = no
        if key:
            elt = key(elt)
        lst.append(elt)
    return yes, no

def make_ranges(length, step):
    """Make non-overlapping ranges of size at most step, from 0 to length.
    Ranges are (start, end) tuples where start and end are inclusive.
    This is probably best demonstrated by example:
    >>> make_ranges(1050, 200)
    [(0, 199), (200, 399), (400, 599), (600, 799), (800, 999), (1000, 1049)]"""
    ranges = []
    count = 0
    while count < length:
        end = min(count + step, length)
        r = (count, end - 1)
        ranges.append(r)
        count += step
    return ranges

def window(seq, n=3, pad=None):
    ngram = [pad] * n
    for word in seq:
        ngram.pop(0)
        ngram.append(word)
        yield tuple(ngram)
    for x in range(n - 1):
        ngram.pop(0)
        ngram.append(pad)
        yield tuple(ngram)

def display_index_every_K_items(seq, k, output_stream=None, format='%s\n'):
    """Provides status messages while you iterate over seq -- every k items,
    it will print the index to output_stream which defaults to stdout.
    format will be interpolated with the index."""
    import sys
    output_stream = output_stream or sys.stdout
    for index, value in enumerate(seq):
        if index % k == 0:
            output_stream.write('%s\n' % index)
            output_stream.flush()
        yield value

def display_marker_every_K_items(seq, k, marker='.', output_stream=None):
    """Provides status messages while you iterate over seq -- every k items,
    it will print marker to output_stream which defaults to stdout."""
    import sys
    output_stream = output_stream or sys.stdout
    for index, value in enumerate(seq):
        if index % k == 0:
            output_stream.write(marker)
            output_stream.flush()
        yield value
    output_stream.write('\n')

if __name__ == "__main__":
    def simple_generator():
        while 1:
            yield 1
    s = display_marker_every_K_items(display_marker_every_K_items(simple_generator(), 100, marker='+'), 10)
    import time
    for x in s:
        time.sleep(0.001) # standing in for real work
