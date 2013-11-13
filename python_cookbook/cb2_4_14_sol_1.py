def invert_dict(d):
    return dict([ (v, k) for k, v in d.iteritems() ])
