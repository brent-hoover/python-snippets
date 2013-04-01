"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66472
Title: frange(), a range function with float increments
Submitter: Dinu Gherman (other recipes)
Last Updated: 2001/08/07
Version no: 1.0
Category: Shortcuts
	
Description:

Sadly missing in the Python standard library, this function allows to use
ranges, just as the built-in function range(), but with float arguments.

All thoretic restrictions apply, but in practice this is more useful
than in theory."""

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L

def xfrange(start, end=None, inc=None):
    """A range function, that does accept float increments and is a
    generator (i.e. lazy)"""

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    count = 0
    while 1:
        next = start + count * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break

        yield next
        count += 1
