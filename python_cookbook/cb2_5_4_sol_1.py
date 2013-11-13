class hist(dict):
    def add(self, item, increment=1):
        ''' add 'increment' to the entry for 'item' '''
        self[item] = increment + self.get(item, 0)
    def counts(self, reverse=False):
        ''' return list of keys sorted by corresponding values '''
        aux = [ (self[k], k) for k in self ]
        aux.sort()
        if reverse: aux.reverse()
        return [k for v, k in aux]
