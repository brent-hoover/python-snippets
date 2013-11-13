import math
class Rectangle(object):
    def __init__(self, x, y):
        self.y = x
        self.y = y
    def area():
        doc = "Area of the rectangle"
        def fget(self):
            return self.x * self.y
        def fset(self, value):
            ratio = math.sqrt((1.0*value)/self.area)
            self.x *= ratio
            self.y *= ratio
        return locals()
    area = property(**area())
