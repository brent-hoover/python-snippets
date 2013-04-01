#!/usr/bin/env python
#
# [SNIPPET_NAME: Combo Box Grid Span]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a combo box grid span]

import pygtk
pygtk.require('2.0')
import gtk

class ComboBoxWrapExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        combobox = gtk.ComboBox()
        liststore = gtk.ListStore(str, int, int)
        cell = gtk.CellRendererText()
        combobox.pack_start(cell)
        combobox.add_attribute(cell, 'text', 0)
        window.add(combobox)
        combobox.set_wrap_width(5)
        for n in range(10):
            liststore.append(['Item %d'%n, n%2+1, n%2+1])
            print liststore[n][1], liststore[n][2]
        combobox.set_model(liststore)
        combobox.set_row_span_column(1)
        combobox.set_column_span_column(2)
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
