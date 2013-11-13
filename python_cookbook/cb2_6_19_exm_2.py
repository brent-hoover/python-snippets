class Base1(object):
    def met(self):
        print 'met in Base1'
class Der1(Base1):
    def met(self):
        s = super(Der1, self)
        if hasattr(s, 'met'):
            s.met()
        print 'met in Der1'
class Base2(object):
    pass
class Der2(Base2):
    def met(self):
        s = super(Der2, self)
        if hasattr(s, 'met'):
            s.met()
        print 'met in Der2'
Der1().met()
Der2().met()
