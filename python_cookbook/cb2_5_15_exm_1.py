def groupnames(name_iterable):
    name_dict = {}
    for name in name_iterable:
        key = _groupkeyfunc(name)
        name_dict.setdefault(key, []).append(name)
    for k, v in name_dict.iteritems():
        aux = [(_sortkeyfunc(name), name) for name in v]
        aux.sort()
        name_dict[k] = tuple([ n for __, n in aux ])
    return name_dict
