def addword(theIndex, word, pagenumber):
    theIndex.setdefault(word, []).append(pagenumber)
