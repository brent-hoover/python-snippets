#!/usr/bin/env python
#
# [SNIPPET_NAME: Entry Completion]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using the Entry Completion widget]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-EntryCompletion.html, http://www.pygtk.org/docs/pygtk/class-gtkentrycompletion.html]

import time
import pygtk
pygtk.require('2.0')
import gtk

class EntryCompletionExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox()
        label = gtk.Label('Type a, b, c or d\nfor completion')
        vbox.pack_start(label)
        entry = gtk.Entry()
        vbox.pack_start(entry)
        window.add(vbox)
        completion = gtk.EntryCompletion()
        self.liststore = gtk.ListStore(str)
        for s in ['apple', 'banana', 'cap', 'comb', 'color',
                  'dog', 'doghouse']:
            self.liststore.append([s])
        completion.set_model(self.liststore)
        entry.set_completion(completion)
        completion.set_text_column(0)
        completion.connect('match-selected', self.match_cb)
        entry.connect('activate', self.activate_cb)
        window.show_all()
        return

    def match_cb(self, completion, model, iter):
        print model[iter][0], 'was selected'
        return

    def activate_cb(self, entry):
        text = entry.get_text()
        if text:
            if text not in [row[0] for row in self.liststore]:
                self.liststore.append([text])
                entry.set_text('')
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = EntryCompletionExample()
    main()
