"""Lets you treat an interator as a list by filling in the list on demand."""

class LazyList:
    def __init__(self, iterator, use_partial_list=False):
        self.list_so_far = []
        self.iterator = iterator
        self.iterator_exhausted = False
        self.use_partial_list = use_partial_list
    def __getitem__(self, index):
        # TODO doesn't handle slices currently -- reads entire list whenever
        # you ask for these!
        if not self.iterator_exhausted:
            if index < 0:
                self._read_all()
            if index >= len(self.list_so_far):
                self._read_many(index - len(self.list_so_far) + 1)

        return self.list_so_far[index]
    def _read_many(self, count):
        for x in range(count):
            self._read_iterator()
            if self.iterator_exhausted:
                break
    def _read_all(self):
        while not self.iterator_exhausted:
            self._read_iterator()
    def _read_iterator(self):
        try:
            self.list_so_far.append(self.iterator.next())
        except StopIteration:
            self.iterator_exhausted = True

    def __getattr__(self, attr):
        if not self.use_partial_list:
            self._read_all()
        return getattr(self.list_so_far, attr)

if __name__ == "__main__":
    def g():
        for x in range(10):
            print 'yield', x
            yield x

    l = LazyList(g())
    print l[4]
    print l[0]
    print l[2:5]
    print l[-1]
    print len(l)
    print repr(l)
    print len(l)
