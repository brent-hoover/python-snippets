def containsOnly(seq, aset):
    """ Check whether sequence seq contains ONLY items in aset. """
    for c in seq:
        if c not in aset: return False
    return True
