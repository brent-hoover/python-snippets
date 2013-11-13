import random
def qsort(L):
    if not L: return L
    pivot = random.choice(L)
    def lt(x): return x<pivot
    def gt(x): return x>pivot
    return qsort(filter(lt, L))+[pivot]*L.count(pivot)+qsort(filter(gt, L))
