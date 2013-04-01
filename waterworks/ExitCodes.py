"""Create textual descriptions of exit statuses."""
__author__ = "David McClosky (dmcc AT cs.brown.edu)"

import os, signal

def signum_to_name(signum):
    for obj in dir(signal):
        if obj.startswith('SIG') and signum == getattr(signal, obj):
            return obj
    else:
        return None

class ExitCode(Exception):
    """Represents the exit code of a spawned command."""
    def __init__(self, exitcode, message=''):
        """exitcode is the exit status of a command, message is a
        description which will be prepended in the str() of this."""
        self.exitcode = exitcode
        self.message = message
        self.exitstatus = None
        self.exited = None
        self.killedbysignalnum = None
        self.killedbysignal = None
        self.stoppedbysignalnum = None
        self.stoppedbysignal = None
        self.coredumped = os.WCOREDUMP(exitcode)

        if os.WIFEXITED(exitcode):
            self.exited = True
            self.exitstatus = os.WEXITSTATUS(exitcode)
        if os.WIFSIGNALED(exitcode):
            self.killedbysignalnum = os.WTERMSIG(exitcode)
            self.killedbysignal = signum_to_name(self.killedbysignalnum)
        if os.WIFSTOPPED(exitcode):
            self.stoppedbysignalnum = os.WSTOPSIG(self.exitcode)
            self.stoppedbysignal = signum_to_name(self.stoppedbysignalnum)
    def describe(self, exitcodedescs=None):
        desc = []
        if self.killedbysignalnum:
            if self.killedbysignal:
                signame = " (%s)" % self.killedbysignal
            else:
                signame = ""
            desc.append("Killed by signal %d%s" % (self.killedbysignalnum, 
                                                    signame))
        if self.exited:
            if exitcodedescs and exitcodedescs.get(self.exitcode):
                codedesc = " (%s)" % exitcodedescs.get(self.exitcode)
            else:
                codedesc = ''
            desc.append("Exited with code %d%s" % (self.exitcode, codedesc))
        if self.stoppedbysignalnum:
            if self.stoppedbysignal:
                signame = " (%s)" % self.stoppedbysignal
            else:
                signame = ""
            desc.append("Stopped by signal %d%s" % (self.stoppedbysignalnum, 
                                                    signame))
        if self.coredumped:
            desc.append("coredumped")
        return ', '.join(desc)

    def __repr__(self):
        return "<%s: %s, message=%r>" % (self.__class__.__name__, 
                                         self.exitcode,
                                         self.message)
    def __str__(self):
        return "%s%s (exit status %s)" % \
               (self.message, self.describe(), self.exitcode)

# DEPRECATED
def describe_exit_status(exitstatus, exitcodedescs=None):
    import warnings
    warnings.warn("Use ExitCode instead of describe_exit_status()", 
                  DeprecationWarning)
    desc = []
    if os.WIFSIGNALED(exitstatus):
        signum = os.WTERMSIG(exitstatus)
        signame = signum_to_name(signum)
        if signame:
            signame = " (%s)" % signame
        else:
            signame = ""
        desc.append("Killed by signal %d%s" % (signum, signame))
    if os.WIFEXITED(exitstatus):
        exitcode = os.WEXITSTATUS(exitstatus)
        if exitcodedescs and exitcodedescs.get(exitcode):
            codedesc = " (%s)" % exitcodedescs.get(exitcode)
        else:
            codedesc = ''
        desc.append("Exited with code %d%s" % (exitcode, codedesc))
    if os.WIFSTOPPED(exitstatus):
        desc.append("Stopped by signal %d" % os.WSTOPSIG(exitstatus))
    if os.WCOREDUMP(exitstatus):
        desc.append("coredumped")
    return desc

# a shorter version
describe = describe_exit_status

if __name__ == "__main__":
    import sys
    for status in sys.argv[1:]:
        print status, describe_exit_status(int(status)), ExitCode(int(status))
