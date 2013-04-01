#!/usr/bin/env python
#
# [SNIPPET_NAME: Status Bar]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Adding and using a status bar]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Statusbars.html, http://www.pygtk.org/docs/pygtk/class-gtkstatusbar.html]

# example statusbar.py

import pygtk
pygtk.require('2.0')
import gtk

class StatusbarExample:
    def push_item(self, widget, data):
        buff = " Item %d" % self.count
        self.count = self.count + 1
        self.status_bar.push(data, buff)
        return

    def pop_item(self, widget, data):
        self.status_bar.pop(data)
        return

    def __init__(self):
        self.count = 1
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("PyGTK Statusbar Example")
        window.connect("delete_event", lambda w,e: gtk.main_quit())
 
        vbox = gtk.VBox(False, 1)
        window.add(vbox)
        vbox.show()
          
        self.status_bar = gtk.Statusbar()      
        vbox.pack_start(self.status_bar, True, True, 0)
        self.status_bar.show()

        context_id = self.status_bar.get_context_id("Statusbar example")

        button = gtk.Button("push item")
        button.connect("clicked", self.push_item, context_id)
        vbox.pack_start(button, True, True, 2)
        button.show()              

        button = gtk.Button("pop last item")
        button.connect("clicked", self.pop_item, context_id)
        vbox.pack_start(button, True, True, 2)
        button.show()              

        # always display the window as the last step so it all splashes on
        # the screen at once.
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    StatusbarExample()
    main()
