pyutil -- a library of useful Python functions and classes
==========================================================

Many of these utilities (or their ancestors) were developed for the Mojo
Nation, Mnet, Allmydata.com "Mountain View", Tahoe-LAFS, or SimpleGeo's
products.  (In the case where the code was developed for a for-profit company,
the copyright holder donated the pyutil code to the public under these open
source licences.)


utilities
=========

current
-------

- mathutil.py_ - integer power, floor, ceil, and nearest multiples;
  permute and fit slope
- memutil.py_ - statistics and diagnostics for memory use and garbage
  collection
- platformutil.py_ - get platform including Linux distro; more accurate
  and less noisy than platform.platform()
- strutil.py_ - common prefix and suffix of two strings, and newline
  processing
- assertutil.py_ - test preconditions, postconditions, and assertions
- benchutil.py_ - benchmark a function by running it repeatedly
- fileutil.py_ - work with files and directories
- iputil.py_ - query available local IPv4 addresses
- jsonutil.py_ - wrapper around simplejson which converts decimal
  inputs to Python Decimal objects instead of to Python floats
- lineutil.py_ - remove extra whitespace from files
- testutil.py_ - utilities for use in unit tests, especially in Twisted
- time_format.py_ - date and time formatting operations
- version_class.py_ - parse version strings into a Version Number
  object
- verlib.py_ - utility to compare version strings, by Tarek Ziade

out of shape
------------

I don't currently use these, but I still think they are possibly good
ideas.

- nummedobj.py_ - number objects in order of creation for consistent
  debug output
- observer.py_ - the Observer pattern
- increasing.py_ - an implementation of a monotonically-increasing
  timer; By the way a future, better implementation of this would use
  CLOCK_MONOTONIC or CLOCK_MONOTONIC_RAW if it were available:
  http://stackoverflow.com/questions/1205722/how-do-i-get-monotonic-time-durations-in-python/1205762#1205762
- repeatable_random.py_ - Make the random and time modules
  deterministic, so that executions can be reproducible.
- strutil.py_ - string utilities
- cache.py_ - multiple implementations of a least-recently-used
  in-memory caching strategy, optimized for different sizes (note: I,
  Zooko, nowadays prefer a random-replacement cache eviction strategy
  over least-recently-used because the former has more consistent and
  predictable behavior)
- odict.py_ - ordered dictionary implementation: see PEP 372. Note:
  there is now (as of Python 2.7) an ordered dict implementation in
  the standard library, but I haven't checked if it is as good as this
  one.
- zlibutil.py_ - zlib decompression in limited memory

deprecated
----------

I no longer use these and I don't recommend that you do either.

- logutil.py_ - send log messages to Twisted logger if present, else
  Python library logger
- weakutil.py_ - allows a bound method's object to be GC'd
- twistedutil.py_ - callLater_weakly, a variant of Twisted's callLater
  which interacts more nicely with weakrefs
- PickleSaver.py_ - make all or part of an object persistent, by saving
  it to disk when it's garbage collected
- humanreadable.py_ - an improved version of the builtin repr()
  function
- hashexpand.py_ - cryptographically strong pseudo-random number
  generator based on SHA256
- find_exe.py_ - try different paths in search of an executable
- dictutil.py_ - several specialized dict extensions, as well as some
  convenient functions for working with dicts
- randutil.py_ - various ways to get random bytes
- xor.py_ - xor two same-length strings together

Thanks to Peter Westlake and Ravi Pinjala for help documenting what
these do.



download
========

http://pypi.python.org/pypi/pyutil

issue tracker
=============

http://tahoe-lafs.org/trac/pyutil

darcs repository
================

http://tahoe-lafs.org/source/pyutil/trunk

(To get the latest source, run ``darcs get --lazy http://tahoe-lafs.org/source/pyutil/trunk``.)

tests and benchmarks
====================

To run tests: ``python ./setup.py trial -s pyutil.test.current``.

You can also run the tests with the standard pyunit test runner
instead of trial, but a couple of the tests will fail due to the
absence of Trial's "Skip This Test" feature. You can also run the
tests of the out-of-shape and deprecated modules:

``python ./setup.py trial -s pyutil.test.out_of_shape``

``python ./setup.py trial -s pyutil.test.deprecated``

Or of all modules:

``python ./setup.py trial -s pyutil.test``

Some modules have self-benchmarks provided.  For example, to benchmark
the cache module: ``python -OOu -c 'from pyutil.test import test_cache; test_cache.quick_bench()'``

or for more complete and time-consuming results: ``python -OOu -c 'from pyutil.test import test_cache; test_cache.slow_bench()'``

(The "-O" is important when benchmarking, since cache has extensive
self-tests that are optimized out when -O is included.)


LICENCE
=======

You may use this package under the GNU General Public License, version 2 or, at
your option, any later version.  You may use this package under the Transitive
Grace Period Public Licence, version 1.0, or at your option, any later version.
(You may choose to use this package under the terms of either licence, at your
option.)  You may use this package under the Simple Permissive Licence, version
1 or, at your option, any later version.  See the file COPYING.GPL_ for the
terms of the GNU General Public License, version 2.  See the file
COPYING.TGPPL.html_ for the terms of the Transitive Grace Period Public Licence,
version 1.0.  See the file COPYING.SPL.txt_ for the terms of the Simple
Permissive Licence, version 1.

.. _COPYING.GPL: COPYING.GPL
.. _COPYING.TGPPL.html: COPYING.TGPPL.html
.. _COPYING.SPL.txt: COPYING.SPL.txt

.. _mathutil.py: pyutil/mathutil.py
.. _memutil.py: pyutil/memutil.py
.. _platformutil.py: pyutil/platformutil.py
.. _strutil.py: pyutil/strutil.py
.. _assertutil.py: pyutil/assertutil.py
.. _benchutil.py: pyutil/benchutil.py
.. _fileutil.py: pyutil/fileutil.py
.. _iputil.py: pyutil/iputil.py
.. _jsonutil.py: pyutil/jsonutil.py
.. _lineutil.py: pyutil/lineutil.py
.. _testutil.py: pyutil/testutil.py
.. _time_format.py: pyutil/time_format.py
.. _version_class.py: pyutil/version_class.py
.. _zlibutil.py: pyutil/zlibutil.py
.. _nummedobj.py: pyutil/nummedobj.py
.. _observer.py: pyutil/observer.py
.. _increasing.py: pyutil/increasing.py
.. _repeatable_random.py: pyutil/repeatable_random.py
.. _strutil.py: pyutil/strutil.py
.. _cache.py: pyutil/cache.py
.. _odict.py: pyutil/odict.py
.. _logutil.py: pyutil/logutil.py
.. _weakutil.py: pyutil/weakutil.py
.. _twistedutil.py: pyutil/twistedutil.py
.. _PickleSaver.py: pyutil/PickleSaver.py
.. _humanreadable.py: pyutil/humanreadable.py
.. _hashexpand.py: pyutil/hashexpand.py
.. _find_exe.py: pyutil/find_exe.py
.. _dictutil.py: pyutil/dictutil.py
.. _randutil.py: pyutil/randutil.py
.. _xor.py: pyutil/xor/xor.py
