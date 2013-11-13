if __name__ == '__main__':
    class TestBase(list, SuperMixin):
        # note: no myMethod defined here
        pass
    class MyTest1(TestBase):
        def myMethod(self):
            print "in MyTest1"
            MyTest1.super()
    class MyTest2(TestBase):
        def myMethod(self):
            print "in MyTest2"
            MyTest2.super()
    class MyTest(MyTest1, MyTest2):
        def myMethod(self):
            print "in MyTest"
            MyTest.super()
    MyTest().myMethod()
# emits:
# in MyTest
# in MyTest1
# in MyTest2
