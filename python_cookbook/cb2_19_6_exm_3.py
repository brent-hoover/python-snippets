import itertools
def strider3(p, n):
    return itertools.imap(lambda i: p[i::n], xrange(n))
