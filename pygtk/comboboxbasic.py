#!/usr/bin/env python
#
# [SNIPPET_NAME: Combo Box Basic]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Creating a basic combo box]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-ComboWidget.html, http://www.pygtk.org/docs/pygtk/class-gtkcombobox.html]

import pygtk
pygtk.require('2.0')
import gtk

class ComboBoxExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        combobox = gtk.combo_box_new_text()
        window.add(combobox)
        combobox.append_text('Select a pie:')
        combobox.append_text('Apple')
        combobox.append_text('Cherry')
        combobox.append_text('Blueberry')
        combobox.append_text('Grape')
        combobox.append_text('Peach')
        combobox.append_text('Raisin')
        combobox.connect('changed', self.changed_cb)
        combobox.set_active(0)
        window.show_all()
        return

    def changed_cb(self, combobox):
        model = combobox.get_model()
        index = combobox.get_active()
        if index:
            print 'I like', model[index][0], 'pie'
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = ComboBoxExample()
    main()
