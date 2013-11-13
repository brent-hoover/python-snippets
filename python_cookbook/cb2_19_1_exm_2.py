import math
def frange1(start, end=None, inc=1.0):
    if end == None:
        end = start + 0.0     # Ensure a float value for 'end'
        start = 0.0
    nitems = int(math.ceil((end-start)/inc))
    for i in xrange(nitems):
        yield start + i * inc
