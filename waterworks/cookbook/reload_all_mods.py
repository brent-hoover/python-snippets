# -*- coding: utf-8 -*-
"""
Title: Reloading all modules
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/81731
Submitter: S¿bastien Keim
Last Updated: 2001/10/15
Version no: 1.0
Category: Debugging

Description:

When you create a Python module, you can use a test script wich import
your module. But you probably have noticed that when you run the test
script, it always use the first version of your module even if you made
changes in the code.  This is because the import statement check if
the module is already in memory and do the import stuff only when this
is mandated.

You can use the reload() function but this is quite difficult if you do
changes in a module wich isn't directly imported by your test script.

A good solution could be to remove all modules from memory before running
the test script.  You only have to put some few lines at the start of
your test script.

Minor updates by David McClosky (dmcc at bigasterisk dot com).
"""

import sys
def reload_all_mods():
    global init_modules
    if globals().has_key('init_modules'):
        for m in [x for x in sys.modules.keys() if x not in init_modules]:
            del sys.modules[m]
    else:
        init_modules = sys.modules.keys()
