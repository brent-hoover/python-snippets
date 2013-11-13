def words_of_file(thefilepath, line_to_words=str.split):
    the_file = open(thefilepath):
    for line in the_file:
        for word in line_to_words(line):
            yield word
    the_file.close()
for word in words_of_file(thefilepath):
    dosomethingwith(word)
