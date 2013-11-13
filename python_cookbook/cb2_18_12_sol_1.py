import string
def format(number, radix, digits=string.digits+string.ascii_lowercase):
   """ format the given integer `number' in the given `radix' using the given
       `digits' (default: digits and lowercase ascii letters) """
   if not 2 <= radix <= len(digits):
      raise ValueError, "radix must be in 2..%r, not %r" % (len(digits), radix)
   # build result as a list of digits in natural order (least-significant digit
   # leftmost), at the end flip it around and join it up into a single string
   result = []
   addon = result.append                    # extract bound-method once
   # compute 'sign' (empty for number>=0) and ensure number >= 0 thereafter
   sign = ''
   if number < 0:
      number = -number
      sign = '-'
   elif number == 0:
      sign = '0'
   _divmod = divmod                         # access to locals is faster
   while number:
      # like: rdigit = number % radix; number //= radix
      number, rdigit = _divmod(number, radix)
      # append appropriate string for the digit we just found
      addon(digits[rdigit])
   # append sign (if any), flip things around, and join up into a string
   addon(sign)
   result.reverse()
   return ''.join(result)
