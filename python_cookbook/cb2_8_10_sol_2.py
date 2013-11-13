import unittest
    suite = doctest.DocFileSuite('test_toy.txt')
    unittest.TextTestRunner().run(suite)
