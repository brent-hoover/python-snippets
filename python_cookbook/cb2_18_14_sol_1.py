import math
class Measurement(object):
    ''' models a measurement with % uncertainty, provides arithmetic '''
    def __init__(self, val, perc):
        self.val = val                            # central value
        self.perc = perc                          # % uncertainty
        self.abs = self.val * self.perc / 100.0   # absolute error
    def __repr__(self):
        return "Measurement(%r, %r)" % (self.val, self.perc)
    def __str__(self):
        return "%g+-%g%%" % (self.val, self.perc)
    def _addition_result(self, result, other_abs):
        new_perc = 100.0 * (math.hypot(self.abs, other_abs) / result)
        return Measurement(result, new_perc)
    def __add__(self, other):
        result = self.val + other.val
        return self._addition_result(result, other.abs)
    def __sub__(self, other):
        result = self.val - other.val
        return self._addition_result(result, other.abs)
    def _multiplication_result(self, result, other_perc):
        new_perc = math.hypot(self.perc, other_perc)
        return Measurement(result, new_perc)
    def __mul__(self, other):
        result = self.val * other.val
        return self._multiplication_result(result, other.perc)
    def __div__(self, other):
        result = self.val / other.val
        return self._multiplication_result(result, other.perc)
