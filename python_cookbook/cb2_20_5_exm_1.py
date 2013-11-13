class Rectangle(object):
    def __init__(self, x, y):
        self._x = x                    # don't trigger _setSide prematurely
        self.y = y                     # now trigger it, so area gets computed
    def _setSide(self, attrname, value):
        setattr(self, attrname, value)
        self.area = self._x * self._y
    x = CommonProperty('_x', fset=_setSide, fdel=None)
    y = CommonProperty('_y', fset=_setSide, fdel=None)
