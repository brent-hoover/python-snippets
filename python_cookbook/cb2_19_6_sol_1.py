def strider(p, n):
    """ Split an iterable p into a list of n sublists, repeatedly taking
        the next element of p and adding it to the next sublist.  Example:
        >>> strider('abcde', 3)
        [['a', 'd'], ['b', 'e'], ['c']]
        In other words, strider's result is equal to:
            [list(p[i::n]) for i in xrange(n)]
        if iterabele p is a sequence supporting extended-slicing syntax.
    """
    # First, prepare the result, a list of n separate lists
    result = [ [] for x in xrange(n) ]
    # Loop over the input, appending each item to one of
    # result's lists, in "round robin" fashion
    for i, item in enumerate(p):
        result[i % n].append(item)
    return result
