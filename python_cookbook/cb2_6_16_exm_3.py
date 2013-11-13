adict = {}
    j = 0
    for i in a, b, c:
        adict[i] = j
        j = j + 1
    for i in a, b, c:
        print i, adict[i]
