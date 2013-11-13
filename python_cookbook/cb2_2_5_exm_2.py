import time
def timeo(fun, n=10):
    start = time.clock()
    for i in xrange(n): fun()
    stend = time.clock()
    thetime = stend-start
    return fun.__name__, thetime
import os
def linecount_w():
    return int(os.popen('wc -l nuc').read().split()[0])
def linecount_1():
    return len(open('nuc').readlines())
def linecount_2():
    count = -1
    for count, line in enumerate(open('nuc')): pass
    return count+1
def linecount_3():
    count = 0
    thefile = open('nuc', 'rb')
    while True:
        buffer = thefile.read(65536)
        if not buffer: break
        count += buffer.count('\n')
    return count
for f in linecount_w, linecount_1, linecount_2, linecount_3:
    print f.__name__, f()
for f in linecount_1, linecount_2, linecount_3:
    print "%s: %.2f"%timeo(f)
