if __name__ == '__main__':
    class Example(Borg):
        name = None
        def __init__(self, name=None):
            if name is not None: self.name = name
        def __str__(self): return 'name->%s' % self.name
    a = Example('Lara')
    b = Example()                  # instantiating b shares self.name with a
    print a, b
    c = Example('John Malkovich')  # making c changes self.name of a & b too
    print a, b, c
    b.name = 'Seven'               # setting b.name changes name of a & c too 
    print a, b, c
