$ python -mtimeit -s'from decimal import Decimal as D' 'D("1.2")+D("3.4")'
10000 loops, best of 3: 191 usec per loop
$ python -mtimeit -s'from decimal import Decimal as D' '1.2+3.4'
1000000 loops, best of 3: 0.339 usec per loop
