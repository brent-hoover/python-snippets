def list_get_egfp(L, i, v=None):
    try: return L[i]
    except IndexError: return v
