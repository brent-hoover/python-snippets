msg = string.Template('the square of $number is $square')
for number in range(10):
    square = number * number
    print msg.substitute(locals())
