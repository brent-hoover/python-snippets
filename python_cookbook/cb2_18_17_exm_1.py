def orientation(p, q, r):
    return ((q - p) * (r - p).conjugate()).imag
## ...
        # still points left on both lists, compare slopes of next hull edges
        # being careful to avoid divide-by-zero in slope calculation
        elif ((U[i+1] - U[i]) * (L[j] - L[j-1]).conjugate()).imag > 0:
            i += 1
        else: j -= 1
## ...
def diameter(Points):
    diam, pair = max([(abs(p-q), (p,q)) for p,q in rotatingCalipers(Points)])
    return pair
