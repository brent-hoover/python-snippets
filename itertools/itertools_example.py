# Enjoy Doing It Wrong, 2009.
# License: WTFPL

import itertools

# found using stackoverflow.com/users
bounds = [i*35 for i in (3307, 186, 93, 59, 41, 31, 23)] +\
         [19*35+20, 16*35+20, 13*35+20, 12*35+15, 6*35+4, 4*35-4] + [42, 8, 0]

# His stats
joel_stats = [8, 10, 11, 11, 13, 14, 14, 15, 15, 16, 17, 19, 21, 26, 30]
labels = [i for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50)]

gaps = []
prev = bounds[0]
for bound in bounds:
    gaps.append(prev-bound)
    prev = bound

less_than = gaps[1:-1]

def reputation_repartition(l):
    def careers_subscribers(l):
        return [n*s*.01 for n, s in itertools.izip(l, joel_stats)]
    subscribers = careers_subscribers(l)
