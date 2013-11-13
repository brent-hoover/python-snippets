import itertools
def windows(iterable, length=2, overlap=0):
    it = iter(iterable)
    results = list(itertools.islice(it, length))
    while len(results) == length:
        yield results
        results = results[length-overlap:]
        results.extend(itertools.islice(it, length-overlap))
    if results:
        yield results
if __name__ == '__main__':
    seq = 'foobarbazer'
    for length in (3, 4):
        for overlap in (0, 1):
            print '%d %d: %s' % (length, overlap,
                    map(''.join, windows(seq, length, overlap)))
