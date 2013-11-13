class MyObject(object):
    def __init__(self, n):
        self.n = n
    @CachedAttribute
    def square(self):
        return self.n * self.n
m = MyObject(23)
print vars(m)                               # 'square' not there yet
# emits: {'n': 23}
print m.square                              # ...so it gets computed
# emits: 529
print vars(m)                               # 'square' IS there now
# emits: {'square': 529, 'n': 23}
del m.square                                # flushing the cache
print vars(m)                               # 'square' removed  
# emits: {'n': 23}
m.n = 42
print vars(m)
# emits: {'n': 42}                   # still no 'square'
print m.square                              # ...so gets recomputed
# emits: 1764
print vars(m)                               # 'square' IS there again
# emits: {'square': 1764, 'n': 23}
