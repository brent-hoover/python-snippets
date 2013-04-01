#!/usr/bin/env python
#
# [SNIPPET_NAME: Base]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a base window]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-GettingStarted.html]

# example base.py

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()

    def main(self):
        gtk.main()

print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
