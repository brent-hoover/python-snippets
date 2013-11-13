def __init__(cls, cname, cbases, cdict):
        super(MetaEnsure_foo, cls).__init__(cls, cname, cbases, cdict)
        cls._foo = 23
