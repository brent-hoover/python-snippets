def fib():
    i1 = 0
    i2 = 1
    yield i1
    yield i2
    while True:
        yield i1 + i2
        i1 = i2
        i2 = i1 + i2
        
y = iter(fib())
while True:
    print '%s, ' % y.next()