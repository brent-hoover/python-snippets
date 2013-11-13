def area():
    what_is_area = "Area of the rectangle"
    def compute_area(self):
        return self.x * self.y
    def scale_both_sides(self, value):
        ratio = math.sqrt((1.0*value)/self.area)
        self.x *= ratio
        self.y *= ratio
    return property(compute_area, scale_both_sides, None, what_is_area)
area = area()
