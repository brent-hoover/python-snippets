def cons(car, cdr): return car, cdr
def car(conscell): return conscell[0]
def cdr(conscell): return conscell[1]
def setcar(conscell, value): conscell[0] = value
def setcdr(conscell, value): conscell[1] = value
