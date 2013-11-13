% python timeit.py -s "import random" \
  -s "x=range(100000); random.shuffle(x)" "sorted(x)"
10 loops, best of 3: 152 msec per loop
