def rotatingCalipers(Points):
    ''' Given a list of 2d points, finds all ways of sandwiching the points
        between two parallel lines that touch one point each, and yields the
        sequence of pairs of points touched by each pair of lines.  '''
    U, L = hulls(Points)
    i = 0
    j = len(L) - 1
    while i < len(U) - 1 or j > 0:
        yield U[i], L[j]
        # if all the way through one side of hull, advance the other side
        if i == len(U) - 1:
            j -= 1
        elif j == 0:
            i += 1
        # still points left on both lists, compare slopes of next hull edges
        # being careful to avoid divide-by-zero in slope calculation
        elif (U[i+1][1]-U[i][1]) * (L[j][0]-L[j-1][0]) > \
             (L[j][1]-L[j-1][1]) * (U[i+1][0]-U[i][0]):
            i += 1
        else: j -= 1
