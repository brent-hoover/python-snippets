#!/usr/bin/env python

# [SNIPPET_NAME: Writing generators]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: How to write a function you can iterate on]
# [SNIPPET_AUTHOR: Josh Holland <jrh@joshh.co.uk>
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://docs.python.org/reference/simple_stmts.html#the-yield-statement, http://www.python.org/dev/peps/pep-0255/]

def fibonacci(start=(0, 1), stop=10):
    """Generate an iterator on the first 'stop' Fibonacci numbers, starting with
    the optional pair of numbers given as an argument.

    """
    a, b = start
    while stop:
        yield a         # the magic happens here.
                        # yield acts like return, but control resumes there
                        # on the next iteration
        a, b = b, a + b
        stop -= 1

for num in fibonacci():
    print num
