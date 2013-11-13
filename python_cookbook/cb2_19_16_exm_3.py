def partfast(n):
    # base case of the recursion: zero is the sum of the empty tuple
    if n == 0:
        yield []
        return
    # modify the partitions of n-1 to form the partitions of n
    for p in partfast(n-1):
        p.append(1)
        yield p
        p.pop()
        if p and (len(p) < 2 or p[-2] > p[-1]):
            p[-1] += 1
            yield p
