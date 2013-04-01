"""Collection of function(s) for working with numbers."""

def deNaN(x, default=0):
    """If x is NaN, return default.  Otherwise, return x."""
    if x != x: # a test for NaN-ness
        return default
    else:
        return x

