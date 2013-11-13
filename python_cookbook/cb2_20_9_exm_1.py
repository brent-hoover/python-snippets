class Skidoo(object):
    ''' a mapping which claims to contain all keys, each with a value
        of 23; item setting and deletion are no-ops; you can also call
        an instance with arbitrary positional args, result is 23. '''
    __metaclass__ = MetaInterfaceChecker
    __implements__ = IMinimalMapping, ICallable
    def __getitem__(self, key): return 23
    def __setitem__(self, key, value): pass
    def __delitem__(self, key): pass
    def __contains__(self, key): return True
    def __call__(self, *args): return 23
sk = Skidoo()
