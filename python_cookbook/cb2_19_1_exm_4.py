import math, Numeric
def frange2(start, end=None, inc=1.0, typecode=None):
    if end == None:
        end = start + 0.0     # Ensure a float value for 'end'
        start = 0.0
    nitems = math.ceil((end-start)/inc)
    return Numeric.arange(nitems) * inc + start
