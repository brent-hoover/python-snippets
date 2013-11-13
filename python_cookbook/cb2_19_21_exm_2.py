class groupby(dict):
    def __init__(self, seq, key):
        for value in seq:
            k = key(value)
            self.setdefault(k, []).append(value)
    __iter__ = dict.iteritems
