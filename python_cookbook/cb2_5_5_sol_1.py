import re
re_digits = re.compile(r'(\d+)')
def embedded_numbers(s):
    pieces = re_digits.split(s)             # split into digits/nondigits
    pieces[1::2] = map(int, pieces[1::2])   # turn digits into numbers
    return pieces
def sort_strings_with_embedded_numbers(alist):
    aux = [ (embedded_numbers(s), s) for s in alist ]
    aux.sort()
    return [ s for __, s in aux ]           # convention: __ means "ignore"
