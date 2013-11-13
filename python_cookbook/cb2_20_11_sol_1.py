def makeChainable(func):
    ''' wrapp a method returning None into one returning self '''
    def chainableWrapper(self, *args, **kwds):
        func(self, *args, **kwds)
        return self
    # 2.4 only: chainableWrapper.__name__ = func.__name__
    return chainableWrapper
class MetaChainable(type):
    def __new__(mcl, cName, cBases, cDict):
        # get the "real" base class, then wrap its mutators into the cDict
        for base in cBases:
            if not isinstance(base, MetaChainable):
                for mutator in cDict['__mutators__']:
                    if mutator not in cDict:
                        cDict[mutator] = makeChainable(getattr(base, mutator))
                break
        # delegate the rest to built-in 'type'
        return super(MetaChainable, mcl).__new__(mcl, cName, cBases, cDict)
class Chainable: __metaclass__ = MetaChainable
if __name__ == '__main__':
    # example usage
    class chainablelist(Chainable, list):
        __mutators__ = 'sort reverse append extend insert'.split()
    print ''.join(chainablelist('hello').extend('ciao').sort().reverse())
# emits: oolliheca
