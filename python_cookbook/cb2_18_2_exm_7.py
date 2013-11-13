def fancier_uniquer(seq, f, p):
    """ Keeps "best" item of each f-defined equivalence class, with
        picking function p choosing appropriate (index, item) for each
        equivalence class from the list of all (index, item) pairs in
        that class """
    bunches = {}
    for index, item in enumerate(seq):
        marker = f(item)
        bunches.setdefault(marker, []).append((index, item))
    auxlist = [p(candidates) for candidates in bunches.values()]
    auxlist.sort()
    return [item for index, item in auxlist]
