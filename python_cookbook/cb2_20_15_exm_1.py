import random
import optimize
@optimize.make_constants(verbose=True)
def sample(population, k):
    " Choose `k' unique random elements from a `population' sequence. "
    if not isinstance(population, (list, tuple, str)):
        raise TypeError('Cannot handle type', type(population))
    n = len(population)
    if not 0 <= k <= n:
        raise ValueError, "sample larger than population"
    result = [None] * k
    pool = list(population)
    for i in xrange(k):         # invariant:  non-selected at [0,n-i)
        j = int(random.random() * (n-i))
        result[i] = pool[j]
        pool[j] = pool[n-i-1]   # move non-selected item into vacancy
    return result
