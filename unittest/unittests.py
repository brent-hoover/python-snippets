#!/usr/bin/env python
#
# [SNIPPET_NAME: Unit Tests]
# [SNIPPET_CATEGORIES: Testing, unittest]
# [SNIPPET_DESCRIPTION: Example of basic Python unit testing]
# [SNIPPET_DOCS: http://docs.python.org/library/unittest.html]
# [SNIPPET_AUTHOR: David Futcher <bobbo@ubuntu.com>]
# [SNIPPET_LICENSE: MIT]

import unittest

FIB_STOP = 10

# Adapted from "Writing generators" snippet by Josh Holland <jrh@joshh.co.uk>
def fibonacci(start=(0, 1), stop=FIB_STOP):
    a, b = start
    while stop:
        yield a
        a, b = b, a + b
        stop -= 1

class FibonacciGeneratorTest(unittest.TestCase):
    """ Basic unit test class to check the above Fibonacci generator """

    def setUp(self):
        self.fibs = []
        self.correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        for x in fibonacci():
            self.fibs.append(x)
    
    def testStopping(self):
        # Check the generator stopped when it should have
        self.assertEqual(FIB_STOP, len(self.fibs))

    def testNumbers(self):
        # Check the generated list against our known correct list
        for i in range(len(self.correct)):
            self.assertEqual(self.fibs[i], self.correct[i])

if __name__ == '__main__':
    unittest.main()

