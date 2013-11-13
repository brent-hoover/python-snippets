import collections
class FifoDeque(collections.deque):
    pop = collections.deque.popleft
