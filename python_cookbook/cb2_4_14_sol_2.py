from itertools import izip
def invert_dict_fast(d):
    return dict(izip(d.itervalues(), d.iterkeys()))
