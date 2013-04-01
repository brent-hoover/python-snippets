"""
Title: iterator wrapper, allowing 'pushback' and 'nonzero' test
Submitter: Manuel Garcia (other recipes)
Last Updated: 2007/03/12
Version no: 1.0
Category: Algorithms

Description:

Needed the ability to 'pushback' values back onto an iterator, and also
was able to add a 'nonzero' test to the iterator at the same time.

Discussion:

adapted from:
http://mail.python.org/pipermail/python-dev/2003-October/038955.html
[Python-Dev] generator comprehension syntax,
was: accumulator display syntax
Alex Martelli aleaxit at yahoo.com
Sat Oct 18 05:20:45 EDT 2003

the 'nonzero' test allows you to do quick boolean tests on whether or
not the iterator is empty.
"""
class pushback_wrapper(object):
    """
    
    >>> p = pushback_wrapper(iter([1, 2, 3, 37]))
    >>> L = []
    >>> for x in p:
    ...     L.append(x)
    ...     if x == 2:
    ...         p.pushback(17)
    ...         p.pushback(19)
    >>> L
    [1, 2, 19, 17, 3, 37]
    >>> bool(p)
    False
    >>> p.pushback(17)
    >>> bool(p)
    True
    >>> p.next()
    17
    >>> bool(p)
    False
    >>> p = pushback_wrapper(iter([1, 2]))
    >>> bool(p)
    True
    >>> p.next()
    1
    >>> p.next()
    2
    >>> bool(p)
    False
    >>> p.next()
    Traceback (most recent call last):
    ...
    StopIteration
    >>> bool(p)
    False
    >>> p.pushback(17)
    >>> bool(p)
    True
        
    """
    
    def __init__(self, it):
        self.it = it
        self.pushed_back = []
        
    def __iter__(self):
        return self
    
    def __nonzero__(self):
        
        if self.pushed_back:
            return True
        
        try:
            self.pushed_back.insert(0, self.it.next())
        except StopIteration:
            return False
        else:
            return True
    
    def next(self):
        try:
            return self.pushed_back.pop()
        except IndexError:
            return self.it.next()
        
    def pushback(self, item):
        self.pushed_back.append(item)
