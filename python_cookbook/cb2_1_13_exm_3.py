def split_by(theline, n, lastfield=False):
    # cut up all the needed pieces
    pieces = [theline[k:k+n] for k in xrange(0, len(theline), n)]
    # drop the last piece if too short and not required
    if not lastfield and len(pieces[-1]) < n:
        pieces.pop()
    return pieces
