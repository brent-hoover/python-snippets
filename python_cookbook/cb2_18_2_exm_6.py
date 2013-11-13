def fancy_unique(seq, f, p):
    """ Keeps "best" item of each f-defined equivalence class, with
        picking function p doing pairwise choice of (index, item) """
    representative = {}
    for index, item in enumerate(seq):
        marker = f(item)
        if marker in representative:
            # It's NOT a problem to rebind index and item within the
            # for loop: the next leg of the loop does not use their binding
            index, item = p((index, item), representative[marker])
        representative[marker] = index, item
    # reconstruct sequence order by sorting on indices
    auxlist = representative.values()
    auxlist.sort()
    return [item for index, item in auxlist]
