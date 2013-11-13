% python timeit.py "100**100"
100000 loops, best of 3: 4.04 usec per loop
% python timeit.py "200**200"
100000 loops, best of 3: 9.03 usec per loop
% python timeit.py "100**100" "200**200"
100000 loops, best of 3: 13.1 usec per loop
