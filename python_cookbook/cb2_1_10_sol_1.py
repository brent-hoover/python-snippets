import string
# Make a reusable string of all characters, which does double duty
# as a translation table specifying <q>no translation whatsoever</q>
allchars = string.maketrans('', '')
def makefilter(keep):
    """ Return a function that takes a string and returns a partial copy
        of that string consisting of only the characters in 'keep'.
        Note that `keep' must be a plain string.
    """
    # Make a string of all characters that are not in 'keep': the "set
    # complement" of keep, meaning the string of characters we must delete
    delchars = allchars.translate(allchars, keep)
    # Make and return the desired filtering function (as a closure)
    def thefilter(s):
        return s.translate(allchars, delchars)
    return thefilter
if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print just_vowels('four score and seven years ago')
# emits: ouoeaeeyeaao
    print just_vowels('tiger, tiger burning bright')
# emits: ieieuii
