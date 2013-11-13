import re

def clean_phone(phone):
    _phone = ''
    pat = re.compile('^(\(?)(\d{3})(\)?)[^0-9]*(\d{3})[^0-9]*(\d{4})')
    x = re.search(pat, phone)
    if x is None:
        return x
    for g in x.groups():
        if len(g) > 2:
            _phone += g
    return _phone
    
    
assert(len(clean_phone('3236873265')) == 10)
print clean_phone('323 687 3265')
print clean_phone('323-687-3265')
print clean_phone('(323) 687 3265')

    