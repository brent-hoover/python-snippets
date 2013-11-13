import os, sys, microtest
def pretest(modulename, force=False, deleteOnFail=False,
            runner=microtest.test, verbose=False, log=sys.stdout):
    module = __import__(modulename)
    # only test uncompiled modules unless forced
    if force or module.__file__.endswith('.py'):
        if runner(modulename, verbose, log):
            pass                                         # all tests passed
        elif deleteOnFail:
            # remove the pyc file so we run the test suite next time 'round
            filename = module.__file__
            if filename.endswith('.py'):
                filename = filename + 'c'
            try: os.remove(filename)
            except OSError: pass
