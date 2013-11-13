def fib():
    ''' Unbounded generator for Fibonacci numbers '''
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
if __name__ == "__main__":
    import itertools
    print list(itertools.islice(fib(), 10))
# outputs: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
