#!/usr/bin/env python
#
# [SNIPPET_NAME: Layout]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: A simple widget layout example]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Layout.html]

# example layout.py

import pygtk
pygtk.require('2.0')
import gtk
import random

class LayoutExample:
    def WindowDeleteEvent(self, widget, event):
        # return false so that window will be destroyed
        return False

    def WindowDestroy(self, widget, *data):
        # exit main loop
        gtk.main_quit()

    def ButtonClicked(self, button):
        # move the button
        self.layout.move(button, random.randint(0,500),
                         random.randint(0,500))

    def __init__(self):
        # create the top level window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Layout Example")
        window.set_default_size(300, 300)
        window.connect("delete-event", self.WindowDeleteEvent)
        window.connect("destroy", self.WindowDestroy)
        # create the table and pack into the window
        table = gtk.Table(2, 2, False)
        window.add(table)
        # create the layout widget and pack into the table
        self.layout = gtk.Layout(None, None)
        self.layout.set_size(600, 600)
        table.attach(self.layout, 0, 1, 0, 1, gtk.FILL|gtk.EXPAND,
                     gtk.FILL|gtk.EXPAND, 0, 0)
        # create the scrollbars and pack into the table
        vScrollbar = gtk.VScrollbar(None)
        table.attach(vScrollbar, 1, 2, 0, 1, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK, 0, 0)
        hScrollbar = gtk.HScrollbar(None)
        table.attach(hScrollbar, 0, 1, 1, 2, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK, 0, 0)
        # tell the scrollbars to use the layout widget's adjustments
        vAdjust = self.layout.get_vadjustment()
        vScrollbar.set_adjustment(vAdjust)
        hAdjust = self.layout.get_hadjustment()
        hScrollbar.set_adjustment(hAdjust)
        # create 3 buttons and put them into the layout widget
        button = gtk.Button("Press Me")
        button.connect("clicked", self.ButtonClicked)
        self.layout.put(button, 0, 0)
        button = gtk.Button("Press Me")
        button.connect("clicked", self.ButtonClicked)
        self.layout.put(button, 100, 0)
        button = gtk.Button("Press Me")
        button.connect("clicked", self.ButtonClicked)
        self.layout.put(button, 200, 0)
        # show all the widgets
        window.show_all()

def main():
    # enter the main loop
    gtk.main()
    return 0

if __name__ == "__main__":
    LayoutExample()
    main()
