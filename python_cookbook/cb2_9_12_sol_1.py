import os, popen2, fcntl, select
def makeNonBlocking(fd):
    fl = fcntl.fcntl(fd, os.F_GETFL)
    try:
        fcntl.fcntl(fd, os.F_SETFL, fl | os.O_NDELAY)
    except AttributeError:
        fcntl.fcntl(fd, os.F_SETFL, fl | os.FNDELAY)
def getCommandOutput(command):
    child = popen2.Popen3(command, 1) # Capture stdout and stderr from command
    child.tochild.close()             # don't need to write to child's stdin
    outfile = child.fromchild
    outfd = outfile.fileno()
    errfile = child.childerr
    errfd = errfile.fileno()
    makeNonBlocking(outfd)            # Don't deadlock! Make fd's nonblocking.
    makeNonBlocking(errfd)
    outdata, errdata = [], []
    outeof = erreof = False
    while True:
        to_check = [outfd]*(not outeof) + [errfd]*(not erreof)
        ready = select.select(to_check, [], []) # Wait for input
        if outfd in ready[0]:
            outchunk = outfile.read()
            if outchunk == '':
                outeof = True
            else:
                outdata.append(outchunk)
        if errfd in ready[0]:
            errchunk = errfile.read()
            if errchunk == '':
                erreof = True
            else:
                errdata.append(errchunk)
        if outeof and erreof:
            break
        select.select([],[],[],.1) # Allow a little time for buffers to fill
    err = child.wait()
    if err != 0:
        raise RuntimeError, '%r failed with exit code %d\n%s' % (
            command, err, ''.join(errdata))
    return ''.join(outdata)
def getCommandOutput2(command):
    child = os.popen(command)
    data = child.read()
    err = child.close()
    if err:
        raise RuntimeError, '%r failed with exit code %d' % (command, err)
