class cons(object):
    __slots__ = ('car', 'cdr')
    def __init__(self, car, cdr):
        self.car = car
        self.cdr = cdr
    def __repr__(self):
        return 'cons(%r, %r)' % (self.car, self.cdr)
