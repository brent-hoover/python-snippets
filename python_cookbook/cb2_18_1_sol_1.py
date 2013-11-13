# support 2.3 as well as 2.4
try: set
except NameError: from sets import Set as set
def unique(s):
    """ Return a list of the elements in s in arbitrary order, but without
        duplicates. """
    # Try using a set first, because it's the fastest and will usually work
    try:
        return list(set(s))
     except TypeError:
        pass  # Move on to the next method
    # Since you can't hash all elements, try sorting, to bring equal items
    # together and then weed them out in a single pass
    t = list(s)
    try:
        t.sort()
    except TypeError:
        del t  # Move on to the next method
    else:
        # the sort worked, so we're fine -- do the weeding
        return [x for i, x in enumerate(t) if not i or x != t[i-1]]
    # Brute force is all that's left
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u
