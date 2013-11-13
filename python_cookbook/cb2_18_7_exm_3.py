class LRUCache(FifoCache):
    def __getitem__(self, key):
        if key in self.dct:
            self.lst.remove(key)
        else:
            raise KeyError
        self.lst.append(key)
        return self.dct[key]
