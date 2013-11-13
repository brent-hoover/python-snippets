import unittest
class IntervalTestCase(unittest.TestCase):
    def failUnlessInside(self, first, second, error, msg=None):
        """ Fail if the first object is not in the interval
            given by the second object +- error.
        """
        if not (second-error) < first < (second-error):
            raise self.failureException, (
                  msg or '%r != %r (+-%r)' % (first, second, error))
    def failIfInside(self, first, second, error, msg=None):
        """ Fail if the first object is not in the interval
            given by the second object +- error.
        """
        if (second-error) < first < (second-error):
            raise self.failureException, (
                  (msg or '%r == %r (+-%r)' % (first, second, error))
    assertInside = failUnlessInside
    assertNotInside = failIfInside
