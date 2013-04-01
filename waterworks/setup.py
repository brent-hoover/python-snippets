import os, sys
from distutils.core import setup

if len(sys.argv) < 2:
    sys.argv.append("build")

setup(name = "waterworks",
      version = "0.2.5",
      maintainer = "David McClosky",
      maintainer_email = "dmcc+py (at) bigasterisk.com",
      description = "waterworks: Because everyone has their own utility library",
      packages = ['cookbook', 'waterworks'],
      py_modules = ['AIMA', 'ExitCodes', 'FigUtil', 'Histogram', 'IntRange', 
                    'IntShelve', 'LazyList', 'Selectron', 'Tailer', 'TeXTable', 
                    'ThreadedJobs', 'TkGeomSavers', 'diffprint', 
                    'iterextras', 'ClusterMetrics', 'FunctionPickler', 
                    'HeapQueue', 'PrecRec', 'Probably', 'robust_apply', 
                    'TerminalTitle', 'vimdiff'],
      url='http://cs.brown.edu/~dmcc/software/',
      download_url='http://cs.brown.edu/~dmcc/software/waterworks/waterworks-0.2.5.tar.gz',
)
