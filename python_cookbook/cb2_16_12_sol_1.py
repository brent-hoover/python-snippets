#!/bin/sh
PYTHON=$(which python 2>/dev/null)
if [ x ! -x "x$PYTHON" ] ; then
    echo "python executable not found - cannot continue!"
    exit 1
fi
exec $PYTHON - $0 $@ << END_OF_PYTHON_CODE
import sys
version = sys.version_info[:2]
if version < (2, 3):
    print 'Sorry, need Python 2.3 or better; %s.%s is too old!' % version
sys.path.insert(0, sys.argv[1])
del sys.argv[0:2]
import main
main.main()
END_OF_PYTHON_CODE
