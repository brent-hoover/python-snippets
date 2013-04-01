#!/usr/bin/env python
#
# [SNIPPET_NAME: Expander]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Use an expander widget]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-ExpanderWidget.html, http://www.pygtk.org/docs/pygtk/class-gtkexpander.html]

import time
import pygtk
pygtk.require('2.0')
import gtk

class ExpanderExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        expander = gtk.Expander(None)
        window.add(expander)
        hbox = gtk.HBox()
        image = gtk.Image()
        image.set_from_stock(gtk.STOCK_OPEN, gtk.ICON_SIZE_BUTTON)
        label = gtk.Label(' Folder Time')
        hbox.pack_start(image)
        hbox.pack_start(label)
        expander.set_label_widget(hbox)
        expander.connect('notify::expanded', self.expanded_cb)
        window.show_all()
        return

    def expanded_cb(self, expander, params):
        if expander.get_expanded():
            label = gtk.Label(time.ctime())
            label.show()
            expander.add(label)
        else:
            expander.remove(expander.child)
            #reset the size of the window to its original one
            expander.get_parent().resize(1, 1)
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = ExpanderExample()
    main()
