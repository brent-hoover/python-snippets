def munge4(alist):
    # Extract all bound methods you need (get immediate exception,
    # without partial alteration, if any needed method is missing):
    append = alist.append
    extend = alist.extend
    # Check operations, such as indexing, to get an exception ASAP
    # if signature compatibility is missing:
    try: alist[0] = alist[0]
    except IndexError: pass    # An empty alist is okay
    # Operate: no exceptions are expected from this point onwards
    append(23)
    extend(range(5))
    append(42)
    alist[4] = alist[3]
    extend(range(2))
