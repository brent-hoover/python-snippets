aux = [ (p.real, p.imag) for p in Points ]
    aux.sort()
    Points[:] = [ complex(*p) for p in aux ]
    del aux
