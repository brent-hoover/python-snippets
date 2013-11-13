# an 'old class'
class Bar(AutoReloader):
    def __init__(self, what=23):
       self.old_attribute = what
# a subclass of the old class
class Baz(Bar):
    pass
# instances of the old class & of its subclass
b = Bar()
b2 = Baz()
# we rebuild the class (normally via 'reload', but, here, in-line!):
class Bar(AutoReloader):
    def __init__(self, what=42):
       self.new_attribute = what+100
    def __update__(self):
       # compute new attribute from old ones, then delete old ones
       self.new_attribute = self.old_attribute+100
       del self.old_attribute
    def meth(self, arg):
       # add a new method which wasn't in the old class
       print arg, self.new_attribute
if __name__ == '__main__':
    # now b is "upgraded" to the new Bar class, so we can call 'meth':
    b.meth(1)
    # emits: 1 123
    # subclass Baz is also upgraded, both for existing instances...:
    b2.meth(2)
    # emits: 2 123
    # ...and for new ones:
    Baz().meth(3)
    # emits: 3 142
