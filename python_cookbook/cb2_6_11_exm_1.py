class RingBuffer(object):
    def __init__(self,size_max):
        self.max = size_max
        self.data = []
    def _full_append(self, x):
        self.data[self.cur] = x
        self.cur = (self.cur+1) % self.max
    def _full_get(self):
        return self.data[self.cur:]+self.data[:self.cur]
    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's methods from non-full to full
            self.append = self._full_append
            self.tolist = self._full_get
    def tolist(self):
        return self.data
