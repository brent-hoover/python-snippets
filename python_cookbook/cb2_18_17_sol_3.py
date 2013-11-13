def diameter(Points):
    ''' Given a list of 2d points, returns the pair that's farthest apart. '''
    diam, pair = max( [((p[0]-q[0])**2 + (p[1]-q[1])**2, (p,q))
                      for p,q in rotatingCalipers(Points)] )
    return pair
