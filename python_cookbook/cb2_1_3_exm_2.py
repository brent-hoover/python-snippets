def isStringLike(anobj):
    try: anobj + ''
    except: return False
    else: return True
