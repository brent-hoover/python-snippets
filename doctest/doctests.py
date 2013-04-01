#!/usr/bin/env python
#
# [SNIPPET_NAME: DocTests]
# [SNIPPET_CATEGORIES: Testing, doctest]
# [SNIPPET_DESCRIPTION: Basic example of using Python DocTests]
# [SNIPPET_DOCS: http://docs.python.org/library/doctest.html]
# [SNIPPET_AUTHOR: David Futcher <bobbo@ubuntu.com>]
# [SNIPPET_LICENSE: MIT]

import doctest

def fibonacci(start=(0, 1), stop=10):
    """ Generates the fibonacci sequence up to up to the
        stop'th term (stop=10 will generate up to fib(10))

        >>> fibs = []
        >>> start = (0, 1)
        >>> stop = 10
        >>> fib5 = 3
        >>> fib10 = 34
        >>> for i in fibonacci(start=start, stop=stop):
        ...     fibs.append(i)
        >>> len(fibs)
        10
        >>> fibs[0] == start[0]
        True
        >>> fibs[1] == start[1]
        True
        >>> fibs[4] == fib5
        True
        >>> fibs[9] == fib10
        True
    """
    a, b = start
    while stop:
        yield a
        a, b = b, a + b
        stop -= 1

if __name__ == '__main__':
    doctest.testmod(verbose=True)

