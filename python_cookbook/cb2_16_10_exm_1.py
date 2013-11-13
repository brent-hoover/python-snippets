import itertools
def primes_less_than(N):
    return [ p for p in itertools.chain([2], xrange(3,N,2))
             if 0 not in itertools.imap(
                 lambda x: p % x, itertools.takewhile(
                       lambda v: v*v <= p, this_list() ))]
