"""Collection of functions and classes for working on system processes."""

import select, os, sys
import subprocess

def bettersystem(command, stdout=None, stderr=None):
    """Select-based version of commands.getstatusoutput.  stdout and stderr
    are stream or stream-like objects.  Returns the exit status."""
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, close_fds=True)
    p_out, p_err = p.stdout, p.stderr
    fd_out = p_out.fileno()
    fd_err = p_err.fileno()

    out_finished = False
    err_finished = False
    while 1:
        rlist, _, _ = select.select([p_out, p_err], [], [])
        if not rlist:
            break

        if p_out in rlist:
            output = os.read(fd_out, 1024)
            if output == '':
                out_finished = True
            else:
                stdout.write(output)
                stdout.flush()
        if p_err in rlist:
            output = os.read(fd_err, 1024)
            if output == '':
                err_finished = True
            else:
                stderr.write(output)
                stderr.flush()

        if out_finished and err_finished and p.poll() != -1:
            break

    return p.wait()

# TODO this might not belong here
def selectbasedreader(pollobjs, read_amount=1024, timeout=0.1):
    result = ''
    while 1:
        rlist, _, _ = select.select(pollobjs, [], [], timeout)
        if not rlist:
            continue

        if rlist:
            f = rlist[0]
            # print 'f', f, dir(f)
            output = os.read(f.fileno(), read_amount)
            if not output:
                return
            yield f, output

class Pipe:
    """Captures some common behaviors about running data through a pipe."""
    def __init__(self, command):
        from popen2 import Popen3
        self.pipe = Popen3(command, capturestderr=True)
        self.command = command
    def feed(self, data):
        self.pipe.tochild.write(data)
        self.pipe.tochild.flush()
    def close(self):
        self.pipe.tochild.close()
    def check(self, read_amount=1024, timeout=0, on_not_ready_func=None,
              return_on_finished=True, include_stderr=False):
        # print "check()", self.command
        p_out, p_err = self.pipe.fromchild, self.pipe.childerr
        fd_out = p_out.fileno()
        fd_err = p_err.fileno()
        result = ''
        while 1:
            rlist, _, _ = select.select([p_out, p_err], [], [], timeout)
            # print 'rlist', rlist
            if not rlist:
                if on_not_ready_func is None:
                    # print 'spit ""'
                    yield ''
                else:
                    # print 'func', on_not_ready_func
                    on_not_ready_func()

            if p_out in rlist:
                output = os.read(fd_out, read_amount)
                # print 'yield', repr(output)
                yield output

            if include_stderr and p_err in rlist:
                output = os.read(fd_err, read_amount)
                yield output

            # print 'poll', self.pipe.poll()
            if return_on_finished and self.pipe.poll() != -1:
                # print 'poll', self.pipe.poll()
                return
    def process(self, data, timeout=1, verifier=None, close_after_feed=False):
        """Rechecks with a timeout until there is no more data coming
        from the pipe.  If there are more elaborate cues about when to
        stop reading, you may need to use check() directly.  verifier()
        is a predicate applied to the output.  If it raises an exception,
        we will wait for more data."""
        from cStringIO import StringIO
        self.feed(data)
        if close_after_feed:
            self.close()
        result = ''
        while 1:
            for newdata in self.check(timeout=timeout):
                if result.strip() and newdata == '':
                    break
                result += newdata

            if verifier:
                try:
                    verifier(result)
                    break
                except:
                    pass # loop again, look for more data
            else:
                break
        return result

# yes, these docs are longer than the code
def build_command(executable_filename, options, flags, extra_options=''):
    """Helps build command line arguments.  In our terminology, options
    are flags that take arguments.  Flags do not take arguments.
    
    options is a dictionary of the form (or a list of tuples):
        {optionname: optionvalue}
    If optionvalue is not None or False, we will add
        -optionname optionvalue
    to the command line.

    flags is a dictionary of the form (or a list of tuples):
        {flagname: flagvalue}
    If flagvalue is true, we will add
        -flagname
    to the command line.
    
    extra_options is a place for any extra unhandled options.  This is
    here in case your options/flags are outdated.

    Returns a string."""

    pieces = [executable_filename]
    if isinstance(options, dict):
        options = options.items()
    for value, option in options:
        if value is not None:
            pieces.append('-%s %s' % (option, value))

    if isinstance(flags, dict):
        flags = flags.items()
    for value, flag in flags:
        if value not in (None, False):
            pieces.append('-%s' % flag)

    if extra_options:
        pieces.append(extra_options)

    return ' '.join(pieces)

def search_and_destroy(host, pid, signal=15):
    """Kills a PID on a specific host.  If the host is not this one,
    we'll ssh to that host."""
    import socket

    thismachine = socket.getfqdn()
    if host == thismachine:
        os.kill(pid, signal)
    else:
        os.system('ssh %s "kill -%d %d"' % (host, signal, pid))

if __name__ == "__main__":
    p = Pipe("rev")
    p.feed('splarg')
    p.close()

    import time
    for x in p.check(on_not_ready_func=lambda: time.sleep(0.1),
                     return_on_finished=False):
        print repr(x)
        if x:
            break
