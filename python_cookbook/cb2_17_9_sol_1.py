<m>% gdb /usr/bin/python2.1</m>
(gdb) br _PyImport_LoadDynamicModule
(gdb) run    # start python
(gdb) cont   # repeat until your extension is loaded
(gdb) # you may need an import statement at python's >>> prompt
(gdb) finish # finish loading your extension module
(gdb) br wrap_myfunction  # break at the entry point in your code
(gdb) disable 1   # don't break for any more modules being loaded
(gdb) cont   # back to Python, run things normally from here
