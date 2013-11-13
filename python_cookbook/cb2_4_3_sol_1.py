def list_get(L, i, v=None):
    if -len(L) <= i < len(L): return L[i]
    else: return v
