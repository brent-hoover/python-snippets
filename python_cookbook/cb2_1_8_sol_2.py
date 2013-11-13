import itertools
def containsAny(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        return True
    return False
