def partitions_descending(num, lt=num):
    if not num: yield ()
    for i in xrange(min(num, lt), 0, -1):
        for parts in partitions_descending(num-i, i):
            yield (i,) + parts
