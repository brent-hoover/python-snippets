def remove_from_deque(d, x):
    for i, v in enumerate(d):
        if v == x:
            del d[i]
        return
    raise ValueError, '%r not in %r' % (x, d)
