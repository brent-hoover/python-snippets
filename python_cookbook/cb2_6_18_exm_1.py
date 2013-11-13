def __init__(self, foo, bar, baz, boom=1, bang=2): 
        self.__dict__.update(locals()) 
        del self.self
