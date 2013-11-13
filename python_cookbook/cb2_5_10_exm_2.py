class X(object):
    def __init__(self):
        self.a = self.b = self.c = 23.51
        self.d = random.random()
    def _dats(self):
        return self.a, self.b, self.c, self.d
    def __cmp__(self, oth):
        return cmp(self._dats, oth._dats)
