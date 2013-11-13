import sys

def E(m):
    def _c(*a,**k):
        try:
            return m(*a,**k)
        except:
            return sys.exc_info()[0]
    return _c

def methodToTest(x):
    return 2/x

if __name__ == "__main__":
    assert methodToTest(2)==1
    assert methodToTest(1)==2
    assert E(methodToTest)(0)==ZeroDivisionError

    # alternative way :

    methodToTest = E(methodToTest) # force decoration
    assert methodToTest(1)==2
    assert methodToTest(2)==1
    assert methodToTest(0)==ZeroDivisionError
