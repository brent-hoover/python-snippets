class MetaEnsure_foo(type):
    def __new__(mcl, cname, cbases, cdict):
        # ensure instances of the new class can have a '_foo' attribute
        if '__slots__' in cdict and '_foo' not in cdict['__slots__']:
            cdict['__slots__'] = tuple(cdict['__slots__']) + ('_foo',)
        return super(MetaEnsure_foo, mcl).__new__(mcl, cname, cbases, cdict)
