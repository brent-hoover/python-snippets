prec = 8             # number of decimal digits (must be under 15)
class F(object):
    def __init__(self, value, full=None):
        self.value = float('%.*e' % (prec-1, value))
        if full is None:
            full = self.value
        self.full = full
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return "F(%s, %r)" % (self, self.full)
    def error(self):
        ulp = float('1'+('%.4e' % self.value)[-5:]) * 10 ** (1-prec)
        return int(abs(self.value - self.full) / ulp)
    def __coerce__(self, other):
        if not isinstance(other, F):
            return (self, F(other))
        return (self, other)
    def __add__(self, other):
        return F(self.value + other.value, self.full + other.full)
    def __sub__(self, other):
        return F(self.value - other.value, self.full - other.full)
    def __mul__(self, other):
        return F(self.value * other.value, self.full * other.full)
    def __div__(self, other):
        return F(self.value / other.value, self.full / other.full)
    def __neg__(self):
        return F(-self.value, -self.full)
    def __abs__(self):
        return F(abs(self.value), abs(self.full))
    def __pow__(self, other):
        return F(pow(self.value, other.value), pow(self.full, other.full))
    def __cmp__(self, other):
        return cmp(self.value, other.value)
