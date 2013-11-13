import random, string
class password(object):
    # Any substantial file of English words will do just as well: we
    # just need self.data to be a big string, the text we'll pastiche
    data = open("/usr/share/dict/words").read().lower()
    def renew(self, n, maxmem=3):
        ''' accumulate into self.chars `n' random characters, with a
            maximum-memory "history" of `maxmem` characters back. '''
        self.chars = []
        for i in range(n):
            # Randomly "rotate" self.data
            randspot = random.randrange(len(self.data))
            self.data = self.data[randspot:] + self.data[:randspot]
            # Get the n-gram
            where = -1
            # start by trying to locate the last maxmem characters in
            # self.chars.  If i<maxmem, we actually only get the last
            # i, i.e., all of self.chars -- but that's OK: slicing
            # is quite tolerant in this way, and it fits the algorithm
            locate = ''.join(self.chars[-maxmem:])
            while where<0 and locate:
                # Locate the n-gram in the data
                where = self.data.find(locate)
                # Back off to a shorter n-gram if necessary
                locate = locate[1:]
            # if where==-1 and locate='', we just pick self.data[0] --
            # it's a random item within self.data, tx to the rotation
            c = self.data[where+len(locate)+1]
            # we only want lowercase letters, so, if we picked another
            # kind of character, we just choose a random letter instead
            if not c.islower(): c = random.choice(string.lowercase)
            # and finally we record the character into self.chars
            self.chars.append(c)
    def __str__(self):
        return ''.join(self.chars)
if __name__ == '__main__':
    "Usage: pastiche [passwords [length [memory]]]"
    import sys
    if len(sys.argv)>1: dopass = int(sys.argv[1])
    else: dopass = 8
    if len(sys.argv)>2: length = int(sys.argv[2])
    else: length = 10
    if len(sys.argv)>3: memory = int(sys.argv[3])
    else: memory = 3
    onepass = password()
    for i in range(dopass):
        onepass.renew(length, memory)
        print onepass
