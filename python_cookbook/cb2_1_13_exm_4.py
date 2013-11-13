def split_at(theline, cuts, lastfield=False):
    # cut up all the needed pieces
    pieces = [ theline[i:j] for i, j in zip([0]+cuts, cuts+[None]) ]
    # drop the last piece if not required
    if not lastfield:
        pieces.pop()
    return pieces
