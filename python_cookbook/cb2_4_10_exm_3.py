def addword(theIndex, word, pagenumber):
    theIndex[word] = theIndex.get(word, []) + [pagenumber]
