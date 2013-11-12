#!/usr/bin/env python
import bisect

def sorted_result(iters, cmp_func=None):
    """
    Given N sorted iterators, returns an iterator that combines the input in a
    sorted manner (according to cmp_func). Continues until all iterators are
    exhausted.

    Requires O(N) extra storage space.
    """
    if not cmp_func:
        func = lambda lhs, rhs: cmp(lhs[0], rhs[0])
        insert = bisect.insort_right
    else:
        func = lambda lhs, rhs: cmp_func(lhs[0], rhs[0])
        insert = gen_insert_func(func)
    state = []
    for iter in iters:
        try:
            state.append((iter.next(), iter))
        except StopIteration:
            pass
    state.sort(func)
    while state:
        next, iter = state.pop(0)
        yield next
        try:
            val = iter.next()
            insert(state, (val, iter))
        except StopIteration:
            pass
    raise StopIteration

def gen_insert_func(func):
    def inserter(a, x, lo=0, hi=None):
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if func(x, a[mid]) < 0:
                hi = mid
            else:
                lo = mid+1
        a.insert(lo, x)

    return inserter

if __name__ == '__main__':
    l1 = range(0, 20, 2)
    l2 = range(1, 20, 5)
    l3 = range(1, 20, 3)
    print l1
    print l2
    print l3
    print list(sorted_result((iter(l1), iter(l2), iter(l3))))

