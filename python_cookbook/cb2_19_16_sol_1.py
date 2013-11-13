def partitions(n):
    # base case of the recursion: zero is the sum of the empty tuple
    if n == 0:
        yield ()
        return
    # modify the partitions of n-1 to form the partitions of n
    for p in partitions(n-1):
        yield (1,) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1,) + p[1:]
