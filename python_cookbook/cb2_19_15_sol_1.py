def _combinators(_handle, items, n):
    ''' factored-out common structure of all following combinators '''
    if n==0:
        yield []
        return
    for i, item in enumerate(items):
        this_one = [ item ]
        for cc in _combinators(_handle, _handle(items, i), n-1):
            yield this_one + cc
def combinations(items, n):
    ''' take n distinct items, order matters '''
    def skipIthItem(items, i):
        return items[:i] + items[i+1:]
    return _combinators(skipIthItem, items, n)
def uniqueCombinations(items, n):
    ''' take n distinct items, order is irrelevant '''
    def afterIthItem(items, i):
        return items[i+1:]
    return _combinators(afterIthItem, items, n)
def selections(items, n):
    ''' take n (not necessarily distinct) items, order matters '''
    def keepAllItems(items, i):
        return items
    return _combinators(keepAllItems, items, n)
def permutations(items):
    ''' take all items, order matters '''
    return combinations(items, len(items))
if __name__=="__main__":
    print "Permutations of 'bar'"
    print map(''.join, permutations('bar'))
# emits ['bar', 'bra', 'abr', 'arb', 'rba', 'rab']
    print "Combinations of 2 letters from 'bar'"
    print map(''.join, combinations('bar', 2))
# emits ['ba', 'br', 'ab', 'ar', 'rb', 'ra']
    print "Unique Combinations of 2 letters from 'bar'"
    print map(''.join, uniqueCombinations('bar', 2))
# emits ['ba', 'br', 'ar']
    print "Selections of 2 letters from 'bar'"
    print map(''.join, selections('bar', 2))
# emits ['bb', 'ba', 'br', 'ab', 'aa', 'ar', 'rb', 'ra', 'rr']
