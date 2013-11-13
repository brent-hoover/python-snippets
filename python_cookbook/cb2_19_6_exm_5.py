import itertools
def strider5(p, n):
    result = [ [] for x in itertools.repeat(0, n) ]
    resiter = itertools.cycle(result)
    for item, sublist in itertools.izip(p, resiter):
        sublist.append(item)
    return result
