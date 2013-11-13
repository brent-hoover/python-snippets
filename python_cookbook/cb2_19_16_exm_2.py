yield p + (1,)
    if p and (len(p) < 2 or p[-2] > p[-1]):
        yield p[:-1] + (p[-1] + 1,)
