import os, tempfile
def getCommandOutput(command):
    outfile = tempfile.mktemp()
    errfile = tempfile.mktemp()
    cmd = "( %s ) > %s 2> %s" % (command, outfile, errfile)
    err = os.system(cmd) >> 8
    try:
        if err != 0:
            raise RuntimeError, '%r failed with exit code %d\n%s' % (
                command, err, file(errfile).read())
        return file(outfile).read()
    finally:
        os.remove(outfile)
        os.remove(errfile)
