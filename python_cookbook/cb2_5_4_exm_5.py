sentence = ''' Hello there this is a test.  Hello there this was a test,
           but now it is not. '''
words = sentence.split()
c = hist()
for word in words: c.add(word)
print "Ascending count:"
print c.counts()
print "Descending count:"
print c.counts(reverse=True)
