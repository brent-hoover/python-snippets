_templist = ## some iterable
    if len(_templist) != 1:
        raise ValueError, 'too many values to unpack'
    name = _templist[0]
    del _templist
