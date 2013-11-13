def canonicform(s):
    """ Given a string s, return s's characters as a canonic-form string:
        alphabetized and without duplicates. """
    return makefilter(s)(allchars)
