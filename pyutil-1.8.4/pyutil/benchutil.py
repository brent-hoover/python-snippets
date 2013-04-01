#  Copyright (c) 2002-2010 Zooko Wilcox-O'Hearn
#  This file is part of pyutil; see README.rst for licensing terms.

"""
Benchmark a function for its behavior with respect to N.

How to use this module:

1. Define a function which runs the code that you want to benchmark. The
function takes a single argument which is the size of the task (i.e. the "N"
parameter). Pass this function as the first argument to rep_bench(), and N as
the second, e.g.:

>>> from pyutil.benchutil import rep_bench
>>> def fib(N):
...  if N <= 1:
...   return 1
...  else:
...   return fib(N-1) + fib(N-2)
...
>>> rep_bench(fib, 25, UNITS_PER_SECOND=1000)
best: 1.968e+00,   3th-best: 1.987e+00, mean: 2.118e+00,   3th-worst: 2.175e+00, worst: 2.503e+00 (of     10)

The output is reporting the number of milliseconds that executing the function
took, divided by N, from ten different invocations of fib(). It reports the
best, worst, M-th best, M-th worst, and mean, where "M" is the natural log of
the number of invocations (in this case 10).

2. Now run it with different values of N and look for patterns:

>>> for N in 1, 5, 9, 13, 17, 21:
...  print "%2d" % N,
...  rep_bench(fib, N, UNITS_PER_SECOND=1000000)
... 
 1 best: 9.537e-01,   3th-best: 9.537e-01, mean: 1.121e+00,   3th-worst: 1.192e+00, worst: 2.146e+00 (of     10)
 5 best: 5.722e-01,   3th-best: 6.199e-01, mean: 7.200e-01,   3th-worst: 8.106e-01, worst: 8.106e-01 (of     10)
 9 best: 2.437e+00,   3th-best: 2.464e+00, mean: 2.530e+00,   3th-worst: 2.570e+00, worst: 2.676e+00 (of     10)
13 best: 1.154e+01,   3th-best: 1.168e+01, mean: 5.638e+01,   3th-worst: 1.346e+01, worst: 4.478e+02 (of     10)
17 best: 6.230e+01,   3th-best: 6.247e+01, mean: 6.424e+01,   3th-worst: 6.460e+01, worst: 7.294e+01 (of     10)
21 best: 3.376e+02,   3th-best: 3.391e+02, mean: 3.521e+02,   3th-worst: 3.540e+02, worst: 3.963e+02 (of     10)
>>> print_bench_footer(UNITS_PER_SECOND=1000000)
all results are in time units per N
time units per second: 1000000; seconds per time unit: 0.000001

(The pattern here is that as N grows, the time per N grows.)

2. If you need to do some setting up before the code can run, then put the
setting-up code into a separate function so that it won't be included in the
timing measurements. A good way to share state between the setting-up function
and the main function is to make them be methods of the same object, e.g.:

>>> import random
>>> class O:
...  def __init__(self):
...   self.l = []
...  def setup(self, N):
...   del self.l[:]
...   self.l.extend(range(N))
...   random.shuffle(self.l)
...  def sort(self, N):
...   self.l.sort()
...
>>> o = O()
>>> for N in 1000, 10000, 100000, 1000000:
...  print "%7d" % N,
...  rep_bench(o.sort, N, o.setup)
...
   1000 best: 4.830e+02,   3th-best: 4.950e+02, mean: 5.730e+02,   3th-worst: 5.858e+02, worst: 7.451e+02 (of     10)
  10000 best: 6.342e+02,   3th-best: 6.367e+02, mean: 6.678e+02,   3th-worst: 6.851e+02, worst: 7.848e+02 (of     10)
 100000 best: 8.309e+02,   3th-best: 8.338e+02, mean: 8.435e+02,   3th-worst: 8.540e+02, worst: 8.559e+02 (of     10)
1000000 best: 1.327e+03,   3th-best: 1.339e+03, mean: 1.349e+03,   3th-worst: 1.357e+03, worst: 1.374e+03 (of     10)

3. Useful fact! rep_bench() returns a dict containing the numbers.

4. Things to fix:

 a. I used to have it hooked up to use the "hotshot" profiler on the code being
 measured. I recently tried to change it to use the newer cProfile profiler
 instead, but I don't understand the interface to cProfiler so it just gives an
 exception if you pass profile=True. Please fix this and send me a patch.

 b. Wouldn't it be great if this script emitted results in a json format that
 was understood by a tool to make pretty interactive explorable graphs? The
 pretty graphs could look like those on http://speed.pypy.org/ . Please make
 this work and send me a patch!
"""

import cProfile, math, operator, sys, time
from decimal import Decimal as D

#from pyutil import jsonutil as json

if not hasattr(time, "realtime"):
    if sys.platform in ("win32", "cygwin",):
        time.realtime = time.clock
    else:
        time.realtime = time.time

from assertutil import _assert

def makeg(func):
    def blah(n, func=func):
        for i in xrange(n):
            func()
    return blah

def rep_bench(func, n, initfunc=None, MAXREPS=10, MAXTIME=60.0, profile=False, profresults="pyutil-benchutil.prof", UNITS_PER_SECOND=1):
    """
    Will run the func up to MAXREPS times, but won't start a new run if MAXTIME
    (wall-clock time) has already elapsed (unless MAXTIME is None).
    """
    assert isinstance(n, int), (n, type(n))
    starttime = time.realtime()
    tls = [] # elapsed time in nanoseconds
    while ((len(tls) < MAXREPS) or (MAXREPS is None)) and ((MAXTIME is None) or ((time.realtime() - starttime) < MAXTIME)):
        if initfunc:
            initfunc(n)
        try:
            tl = bench_it(func, n, profile=profile, profresults=profresults)
        except BadMeasure:
            pass
        else:
            tls.append(tl * UNITS_PER_SECOND)
    assert tls
    sumtls = reduce(operator.__add__, tls)
    mean = sumtls / len(tls)
    tls.sort()
    worst = tls[-1]
    best = tls[0]
    m = min(int(math.log(len(tls)))+1, len(tls))
    mthworst = tls[-m]
    mthbest = tls[m-1]

    res = {
        'worst': worst/n,
        'best': best/n,
        'm': m,
        'mth-best': mthbest/n,
        'mth-worst': mthworst/n,
        'mean': mean/n,
        'num': len(tls),
        }

    print "best: %(best)#8.03e, %(m)3dth-best: %(mth-best)#8.03e, mean: %(mean)#8.03e, %(m)3dth-worst: %(mth-worst)#8.03e, worst: %(worst)#8.03e (of %(num)6d)" % res

    return res

MARGINOFERROR = 10

worstemptymeasure = 0

class BadMeasure(Exception):
    """ Either the clock wrapped (which happens with time.clock()) or
    it went backwards (which happens with time.time() on rare
    occasions), (or the code under measure completed before a single
    clock tick, which is probably impossible). """
    pass

def do_nothing(n):
    pass

def bench_it(func, n, profile=False, profresults="pyutil-benchutil.prof"):
    if profile:
        st = time.realtime()
        cProfile.run('func(n)', profresults)
        sto = time.realtime()
    else:
        st = time.realtime()
        func(n)
        sto = time.realtime()
    timeelapsed = sto - st
    if timeelapsed <= 0:
        raise BadMeasure(timeelapsed)
    global worstemptymeasure
    emsta = time.realtime()
    do_nothing(2**32)
    emstop = time.realtime()
    empty = emstop - emsta
    if empty > worstemptymeasure:
        worstemptymeasure = empty
    _assert(timeelapsed*MARGINOFERROR > worstemptymeasure, "Invoking func %s(%s) took only %0.20f seconds, but we cannot accurately measure times much less than %0.20f seconds.  Therefore we cannot produce good results here.  Try benchmarking a more time-consuming variant." % (func, n, timeelapsed, worstemptymeasure,))
    return timeelapsed

def bench(func, initfunc=None, TOPXP=21, MAXREPS=5, MAXTIME=60.0, profile=False, profresults="pyutil-benchutil.prof", outputjson=False, jsonresultsfname="pyutil-benchutil-results.json", UNITS_PER_SECOND=1):
    BSIZES = []
    for i in range(TOPXP-6, TOPXP+1, 2):
        n = int(2 ** i)
        if n < 1:
            n = 1
        if BSIZES and n <= BSIZES[-1]:
            n *= 2
        BSIZES.append(n)

    res = {}
    for BSIZE in BSIZES:
        print "N: %7d," % BSIZE,
        sys.stdout.flush()
        r = rep_bench(func, BSIZE, initfunc=initfunc, MAXREPS=MAXREPS, MAXTIME=MAXTIME, profile=profile, profresults=profresults, UNITS_PER_SECOND=UNITS_PER_SECOND)
        res[BSIZE] = r

    #if outputjson:
    #    write_file(jsonresultsfname, json.dumps(res))

    return res

def print_bench_footer(UNITS_PER_SECOND=1):
    print "all results are in time units per N"
    print "time units per second: %s; seconds per time unit: %s" % (UNITS_PER_SECOND, D(1)/UNITS_PER_SECOND)
