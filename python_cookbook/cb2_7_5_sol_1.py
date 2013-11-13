import cPickle
class Greeter(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print 'hello', self.name
class Repeater(object):
    def __init__(self, greeter):
        self.greeter = greeter
    def greet(self):
        self.greeter()
        self.greeter()
r = Repeater(Greeter('world').greet)
