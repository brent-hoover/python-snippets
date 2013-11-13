code = """
def testFunc():
    print "spam!"
class testClass(object):
    def testMethod(self):
        print "eggs!"
"""
m = importCode(code, "test")
m.testFunc()
o = m.testClass()
o.testMethod()
