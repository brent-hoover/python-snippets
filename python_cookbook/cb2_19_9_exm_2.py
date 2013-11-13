def cross_two(a, b):
    for x in a:
        for y in b:
            yield a, b
