import unittest

class A:
    pass

class B1(A):
    pass

class B2(A):
    pass

class C(B1, B2):
    pass

class D(B1):
    pass

class E(D, B2):
    pass

class TestNewIsInstance(unittest.TestCase):
    def setUp(self):
        self.a = A()
        self.b1 = B1()
        self.b2 = B2()
        self.c = C()
        self.d = D()
        self.e = E()

    def testbasic(self):
        self.failUnless(new_isinstance(self.a, A))
        self.failUnless(new_isinstance(self.a, [A]))
        self.failUnless(new_isinstance(self.a, [A, B1]))
        self.failUnless(new_isinstance(self.a, [B1, A]))
        self.failUnless(new_isinstance(self.a, [A, int]))
        self.failUnless(new_isinstance(self.a, [int, A]))
        self.failIf(new_isinstance(self.a, int))
        self.failIf(new_isinstance(self.a, [int]))
        self.failIf(new_isinstance(self.a, []))

    def testhier(self):
        self.failUnless(new_isinstance(self.b1, A))
        self.failUnless(new_isinstance(self.b2, A))
        self.failUnless(new_isinstance(self.c, A))
        self.failUnless(new_isinstance(self.d, A))
        self.failUnless(new_isinstance(self.e, A))

        self.failUnless(new_isinstance(self.b1, B1))
        self.failUnless(new_isinstance(self.c, B1))
        self.failUnless(new_isinstance(self.d, B1))
        self.failUnless(new_isinstance(self.e, B1))
        self.failIf(new_isinstance(self.a, B1))
        self.failIf(new_isinstance(self.b2, B1))

        self.failUnless(new_isinstance(self.b2, B2))
        self.failUnless(new_isinstance(self.c, B2))
        self.failUnless(new_isinstance(self.e, B2))
        self.failIf(new_isinstance(self.a, B2))
        self.failIf(new_isinstance(self.b1, B2))
        self.failIf(new_isinstance(self.d, B2))

        self.failUnless(new_isinstance(self.c, C))
        self.failIf(new_isinstance(self.a, C))
        self.failIf(new_isinstance(self.b1, C))
        self.failIf(new_isinstance(self.b2, C))
        self.failIf(new_isinstance(self.d, C))
        self.failIf(new_isinstance(self.e, C))

        self.failUnless(new_isinstance(self.d, D))
        self.failUnless(new_isinstance(self.e, D))
        self.failIf(new_isinstance(self.a, D))
        self.failIf(new_isinstance(self.b1, D))
        self.failIf(new_isinstance(self.b2, D))
        self.failIf(new_isinstance(self.c, D))

        self.failUnless(new_isinstance(self.e, D))
        self.failUnless(new_isinstance(self.d, D))
        self.failIf(new_isinstance(self.a, D))
        self.failIf(new_isinstance(self.b1, D))
        self.failIf(new_isinstance(self.b2, D))
        self.failIf(new_isinstance(self.c, D))

    def testbuiltins(self):
        self.failIf(new_isinstance('hi', D))
        self.failIf(new_isinstance([], D))
        self.failIf(new_isinstance({}, D))
        self.failIf(new_isinstance(37.2, D))

        self.failUnless(new_isinstance('hi', str))
        self.failUnless(new_isinstance([], list))
        self.failUnless(new_isinstance({}, dict))
        self.failUnless(new_isinstance(37.2, float))

if __name__ == "__main__":
    unittest.main()
