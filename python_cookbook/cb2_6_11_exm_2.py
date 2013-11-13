from collections import deque
class RingBuffer(deque):
    def __init__(self, size_max):
        deque.__init__(self)
        self.size_max = size_max
    def append(self, datum):
        deque.append(self, datum)
        if len(self) > self.size_max:
            self.popleft()
    def tolist(self):
        return list(self)
