def itemgetter(i):
    def getter(x): return x[i]
    return getter
def sorted(seq, key):
    aux = [(key(x), i, x) for i, x in enumerate(seq)]
    aux.sort()
    return [x for k, i, x in aux]
