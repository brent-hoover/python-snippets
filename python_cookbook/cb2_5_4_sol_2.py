class hist1(list):
    def __init__(self, n):
        ''' initialize this list to count occurrences of n distinct items '''
        list.__init__(self, n*[0])
    def add(self, item, increment=1):
        ''' add 'increment' to the entry for 'item' '''
        self[item] += increment
    def counts(self, reverse=False):
        ''' return list of indices sorted by corresponding values '''
        aux = [ (v, k) for k, v in enumerate(self) ]
        aux.sort()
        if reverse: aux.reverse()
        return [k for v, k in aux]
