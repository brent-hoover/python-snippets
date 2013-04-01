#!/usr/bin/env python

# pyutil -- utility functions and classes
#
# Author: Zooko Wilcox-O'Hearn
#
# See README.rst for licensing information.

import os, re, sys

try:
    from ez_setup import use_setuptools
except ImportError:
    pass
else:
    use_setuptools(download_delay=0)

from setuptools import find_packages, setup

trove_classifiers=[
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    ]

PKG='pyutil'
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))

setup_requires = []

# setuptools_trial is needed if you want "./setup.py trial" or
# "./setup.py test" to execute the tests.
# http://pypi.python.org/pypi/setuptools_trial
if 'trial' in sys.argv[1:]:
    setup_requires.extend(['setuptools_trial >= 0.5'])

# darcsver is needed only if you want "./setup.py darcsver" to write a new
# version stamp in pyutil/_version.py, with a version number derived from
# darcs history.  http://pypi.python.org/pypi/darcsver
if 'darcsver' in sys.argv[1:]:
    setup_requires.append('darcsver >= 1.0.0')

# setuptools_darcs is required to produce complete distributions (such
# as with "sdist" or "bdist_egg"), unless there is a
# pyutil.egg-info/SOURCE.txt file present which contains a complete
# list of files that should be included.
# http://pypi.python.org/pypi/setuptools_darcs However, requiring it
# runs afoul of a bug in Distribute, which was shipped in Ubuntu
# Lucid, so for now you have to manually install it before building
# sdists or eggs:
# http://bitbucket.org/tarek/distribute/issue/55/revision-control-plugin-automatically-installed-as-a-build-dependency-is-not-present-when-another-build-dependency-is-being
if False:
    setup_requires.append('setuptools_darcs >= 1.1.0')


data_fnames=[ 'COPYING.SPL.txt', 'COPYING.GPL', 'COPYING.TGPPL.html', 'README.rst', 'CREDITS' ]

# In case we are building for a .deb with stdeb's sdist_dsc command, we put the
# docs in "share/doc/python-$PKG".
doc_loc = "share/doc/" + PKG
data_files = [(doc_loc, data_fnames)]

install_requires=['zbase32 >= 1.0']
if sys.version_info < (2, 7):
    install_requires.append('argparse >= 0.8')

setup(name=PKG,
      version=verstr,
      description='a collection of utilities for Python programmers',
      long_description=open('README.rst').read(),
      author='Zooko O\'Whielacronx',
      author_email='zooko@zooko.com',
      url='http://tahoe-lafs.org/trac/' + PKG,
      license='GNU GPL', # see README.rst for details -- there are also alternative licences
      packages=find_packages(),
      include_package_data=True,
      data_files=data_files,
      setup_requires=setup_requires,
      extras_require={'jsonutil': ['simplejson >= 2.1.0',]},
      install_requires=install_requires,
      classifiers=trove_classifiers,
      entry_points = {
          'console_scripts': [
              'randcookie = pyutil.scripts.randcookie:main',
              'tailx = pyutil.scripts.tailx:main',
              'lines = pyutil.scripts.lines:main',
              'randfile = pyutil.scripts.randfile:main',
              'unsort = pyutil.scripts.unsort:main',
              'verinfo = pyutil.scripts.verinfo:main',
              'try_decoding = pyutil.scripts.try_decoding:main',
              ] },
      test_suite=PKG+".test",
      zip_safe=False, # I prefer unzipped for easier access.
      )
