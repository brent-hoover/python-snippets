class Temperature(object):
    coefficients = {'c': (1.0, 0.0, -273.15), 'f': (1.8, -273.15, 32.0),
                    'r': (1.8, 0.0, 0.0)}
    def __init__(self, **kwargs):
        # default to absolute (Kelvin) 0, but allow one named argument,
        # with name being k, c, f or r, to use any of the scales
        try:
            name, value = kwargs.popitem()
        except KeyError:
            # no arguments, so default to k=0
            name, value = 'k', 0
        # error if there are more arguments, or the arg's name is unknown
        if kwargs or name not in 'kcfr':
            kwargs[name] = value             # put it back for diagnosis
            raise TypeError, 'invalid arguments %r' % kwargs
        setattr(self, name, float(value))
    def __getattr__(self, name):
        # maps getting of c, f, r, to computation from k
        try:
            eq = self.coefficients[name]
        except KeyError:
            # unknown name, give error message
            raise AttributeError, name
        return (self.k + eq[1]) * eq[0] + eq[2]
    def __setattr__(self, name, value):
        # maps settings of k, c, f, r, to setting of k; forbids others
        if name in self.coefficients:
            # name is c, f or r -- compute and set k
            eq = self.coefficients[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
            # name is k, just set it
            object.__setattr__(self, name, value)
        else:
            # unknown name, give error message
            raise AttributeError, name
    def __str__(self):
        # readable, concise representation as string
        return "%s K" % self.k
    def __repr__(self):
        # detailed, precise representation as string
        return "Temperature(k=%r)" % self.k
