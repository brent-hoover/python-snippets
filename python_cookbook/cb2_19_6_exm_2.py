def strider2(p, n):
    for i in xrange(n):
        yield p[i::n]
