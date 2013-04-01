"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/497006
Title: zip_exc(), a lazy zip() that ensures that all iterables have the same length
Submitter: Peter Otten
Last Updated: 2006/08/31
Version no: 1.0
Category: Algorithms

Description:

Using zip(names, values) may inadvertently eat some of your data when
there are, e. g., fewer values than names. This is easy to fix with
assert len(names) == len(values) if the arguments' length is known, but
not if they are arbitrary iterables. With zip_exc() no such glitches
go unnoticed as list(zip_exc(names, values)) throws a LengthMismatch
exception if the number of names and values differ.

>>> list(zip_exc([]))
[]

>>> list(zip_exc((), (), ()))
[]

>>> list(zip_exc("abc", range(3)))
[('a', 0), ('b', 1), ('c', 2)]

>>> try:
...     list(zip_exc("", range(3)))
... except LengthMismatch:
...     print "mismatch"
mismatch

>>> try:
...     list(zip_exc(range(3), ()))
... except LengthMismatch:
...     print "mismatch"
mismatch

>>> try:
...     list(zip_exc(range(3), range(2), range(4)))
... except LengthMismatch:
...     print "mismatch"
mismatch

>>> items = zip_exc(range(3), range(2), range(4))
>>> items.next()
(0, 0, 0)
>>> items.next()
(1, 1, 1)
>>> try: items.next()
... except LengthMismatch: print "mismatch"
mismatch

Discussion:

My implementation looks a bit different
than the straightforward approach used in
http://mail.python.org/pipermail/python-3000/2006-March/000160.html,
for example.

To keep the performance hit low, I've tried hard move as much of the
work into code written in C (The chain() and izip() functions from the
marvelous itertools module). I challenge you to come up with something
faster in pure Python :-)
"""

from itertools import chain, izip

class LengthMismatch(Exception):
    pass

def _throw():
    raise LengthMismatch
    yield None # unreachable

def _check(rest):
    for i in rest:
        try:
            i.next()
        except LengthMismatch:
            pass
        else:
            raise LengthMismatch
    return
    yield None # unreachable

def zip_exc(*iterables):
    """Like itertools.izip(), but throws a LengthMismatch exception if
    the iterables' lengths differ.
    """
    rest = [chain(i, _throw()) for i in iterables[1:]]
    first = chain(iterables[0], _check(rest))
    return izip(*[first] + rest)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
