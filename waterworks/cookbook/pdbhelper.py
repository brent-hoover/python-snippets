"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/65287
Title: Automatically start the debugger on an exception
Submitter: Thomas Heller
Last Updated: 2001/07/13
Version no: 1.4
Category: Debugging

Description:

When Python runs a script and an uncatched exception is raised,
a traceback is printed and the script is terminated.  Python2.1 has
introduced sys.excepthook, which can be used to override the handling of
uncaught exceptions. This allows to automatically start the debugger on an
unexpected exception, even if python is not running in interactive mode.

Discussion:

The above code should be included in 'sitecustomize.py', which is
automatically imported by python. The debugger is only started when
python is run in non-interactive mode.

Note by dmcc: To install pdb as your exception hook, just import this module.
It will save the original except hook, which you can restore with 
restore_pdb_excepthook().  You can reenable the pdb hook with 
install_pdb_excepthook()"""

import sys

def pdbexcepthook(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty():
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback, pdb
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print
      # ...then start the debugger in post-mortem mode.
      pdb.pm()

def install_pdb_excepthook():
    global _original_excepthook
    _original_excepthook = sys.excepthook
    sys.excepthook = pdbexcepthook
def restore_pdb_excepthook():
    global _original_excepthook
    sys.excepthook = _original_excepthook

install_pdb_excepthook()
