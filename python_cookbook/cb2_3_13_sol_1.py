import decimal
""" calculate Italian invoice taxes given a subtotal. """
def italformat(value, places=2, curr='EUR', sep='.', dp=',', pos='', neg='-',
               overall=10):
    """ Convert Decimal ``value'' to a money-formatted string.
    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, or blank) every 3
    dp:      decimal point indicator (comma or period); only specify as
                 blank when places is zero
    pos:     optional sign for positive numbers: "+", space or blank
    neg:     optional sign for negative numbers: "-", "(", space or blank
    overall: optional overall length of result, adds padding on the
                 left, between the currency symbol and digits
    """
    q = decimal.Decimal((0, (1,), -places))             # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    append, next = result.append, digits.pop
    for i in range(places):
        if digits:
            append(next())
        else:
            append('0')
    append(dp)
    i = 0
    while digits:
        append(next())
        i += 1
        if i == 3 and digits:
            i = 0
            append(sep)
    while len(result) < overall:
        append(' ')
    append(curr)
    if sign: append(neg)
    else: append(pos)
    result.reverse()
    return ''.join(result)
# get the subtotal for use in calculations
def getsubtotal(subtin=None):
    if subtin == None:
        subtin = input("Enter the subtotal: ")
    subtotal = decimal.Decimal(str(subtin))
    print "\n subtotal:                   ", italformat(subtotal)
    return subtotal
# specific Italian tax law functions
def cnpcalc(subtotal):
    contrib = subtotal * decimal.Decimal('.02')
    print "+ contributo integrativo 2%:    ", italformat(contrib, curr='')
    return contrib
def vatcalc(subtotal, cnp):
    vat = (subtotal+cnp) * decimal.Decimal('.20')
    print "+ IVA 20%:                      ", italformat(vat, curr='')
    return vat
def ritacalc(subtotal):
    rit = subtotal * decimal.Decimal('.20')
    print "-Ritenuta d'acconto 20%:        ", italformat(rit, curr='')
    return rit
def dototal(subtotal, cnp, iva=0, rit=0):
    totl = (subtotal+cnp+iva)-rit
    print "                     TOTALE: ", italformat(totl)
    return totl
# overall calculations report
def invoicer(subtotal=None, context=None):
    if context is None:
        decimal.getcontext().rounding="ROUND_HALF_UP"     # Euro rounding rules
    else:
        decimal.setcontext(context)                       # set to context arg
    subtot = getsubtotal(subtotal)      
    contrib = cnpcalc(subtot)
    dototal(subtot, contrib, vatcalc(subtot, contrib), ritacalc(subtot))
if __name__=='__main__':
    print "Welcome to the invoice calculator"
    tests = [100, 1000.00, "10000", 555.55]
    print "Euro context"
    for test in tests:
        invoicer(test)
    print "default context"
    for test in tests:
        invoicer(test, context=decimal.DefaultContext)
