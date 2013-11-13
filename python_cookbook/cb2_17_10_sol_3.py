debug:
        make clean; make OPT="-g -DPy_DEBUG" all
CFLAGS = $(OPT) -fpic -O2 -I/usr/local/include -I/usr/include/python2.3
