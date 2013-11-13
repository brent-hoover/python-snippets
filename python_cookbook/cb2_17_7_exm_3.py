import timeit, operator
from total import total
from totit import totit
def timo(fn, sq, init):
    T = timeit.Timer('timon.%s(%s)'%(fn,sq), 'import timon\n'+init)
    print ' %5.5s: %5.2f' % (fn, T.timeit(40000))
def totpy(x):
    result = 0.0
    for item in x: result += item
    return result
def totre(x):
    return reduce(operator.add, x, 0.0)
def totsu(x):
    return sum(x, 0.0)
if __name__ == '__main__':
    print 'on lists:'
    for f in 'totre totpy total totit totsu'.split():
        timo(f, 'seq', 'seq=range(2000)')
    print 'on iters:'
    for f in 'totre totpy total totit totsu'.split():
        timo(f, 'g()', 'def g():\n  for x in range(2000): yield x')
