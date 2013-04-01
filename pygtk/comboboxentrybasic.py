#!/usr/bin/env python
#
# [SNIPPET_NAME: Combo Box Entry Basic]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a simple combo box entry widget]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkcomboboxentry.html]

import pygtk
pygtk.require('2.0')
import gtk

class ComboBoxEntryExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        comboboxentry = gtk.combo_box_entry_new_text()
        window.add(comboboxentry)
        comboboxentry.append_text('Apple')
        comboboxentry.append_text('Cherry')
        comboboxentry.append_text('Blueberry')
        comboboxentry.append_text('Grape')
        comboboxentry.append_text('Peach')
        comboboxentry.append_text('Raisin')
        comboboxentry.child.connect('changed', self.changed_cb)
        comboboxentry.set_active(0)
        window.show_all()
        return

    def changed_cb(self, entry):
        print 'I like', entry.get_text(), 'pie'
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = ComboBoxEntryExample()
    main()
