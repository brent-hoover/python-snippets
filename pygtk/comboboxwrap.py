#!/usr/bin/env python
#
# [SNIPPET_NAME: Combo Box Wrap]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a comb box that wraps it's entries]

import pygtk
pygtk.require('2.0')
import gtk

class ComboBoxWrapExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        combobox = gtk.ComboBox()
        liststore = gtk.ListStore(str)
        cell = gtk.CellRendererText()
        combobox.pack_start(cell)
        combobox.add_attribute(cell, 'text', 0)
        window.add(combobox)
        combobox.set_wrap_width(5)
        for n in range(50):
            liststore.append(['Item %d'%n])
        combobox.set_model(liststore)
        combobox.connect('changed', self.changed_cb)
        combobox.set_active(0)
        window.show_all()
        return

    def changed_cb(self, combobox):
        model = combobox.get_model()
        index = combobox.get_active()
        if index > -1:
            print model[index][0], 'selected'
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = ComboBoxWrapExample()
    main()
