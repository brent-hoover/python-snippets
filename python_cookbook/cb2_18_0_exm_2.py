% python timeit.py "100 + 200; 100 - 200"
10000000 loops, best of 3: 0.151 usec per loop
% python timeit.py "100 + 200" "100 - 200"
10000000 loops, best of 3: 0.151 usec per loop
