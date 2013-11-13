def containsAll(seq, aset):
    """ Check whether sequence seq contains ALL the items in aset. """
    return not set(aset).difference(seq)
