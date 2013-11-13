import re
num_re = re.compile(r'^[-+]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][-+]?[0-9]+)?$')
def is_a_number(s):
    return bool(num_re.match(s))
