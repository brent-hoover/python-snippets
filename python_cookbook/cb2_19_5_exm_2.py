def enumgen():
    for x in xrange(how_many_unpacked()): yield x
a, b, c, d, e = enumgen()
