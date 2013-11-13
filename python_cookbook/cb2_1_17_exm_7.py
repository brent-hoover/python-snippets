msg = string.Template('the square of $number is $square')
for number in range(10):
    print msg.substitute(locals(), square=number*number)
