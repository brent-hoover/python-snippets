class M(type):
    def __new__(cls, name, bases, classdict):
        for attr in classdict.get('__slots__', ()):
            if attr.startswith('_'):
                def getter(self, attr=attr): 
                    return getattr(self, attr)
                # 2.4 only: getter.__name__ = 'get' + attr[1:]
                classdict['get' + attr[1:]] = getter
        return type.__new__(cls, name, bases, classdict)
