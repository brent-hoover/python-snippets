def complicated_choice(words):
    def first_letter(aword):
        return aword[0].lower()
    def prefer((indx1, word1), (indx2, word2)):
        if len(word2) > len(word1):
            return indx2, word2
        return indx1, word1
    return fancy_unique(words, first_letter, prefer)
