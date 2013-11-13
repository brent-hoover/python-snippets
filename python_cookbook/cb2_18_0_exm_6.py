% python timeit.py "import random" \
  "x=range(100000); random.shuffle(x)" "sorted(x)"
10 loops, best of 3: 309 msec per loop
