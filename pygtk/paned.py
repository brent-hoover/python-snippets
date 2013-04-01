#!/usr/bin/env python
#
# [SNIPPET_NAME: Paned]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a paned widget]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtktutorial/sec-panedwindowwidgets.html, http://www.pygtk.org/pygtk2tutorial/sec-PanedWindowWidgets.html, http://www.pygtk.org/docs/pygtk/class-gtkpaned.html]

# example paned.py

import pygtk
pygtk.require('2.0')
import gtk, gobject

class PanedExample:
    # Create the list of "messages"
    def create_list(self):
        # Create a new scrolled window, with scrollbars only if needed
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        model = gtk.ListStore(gobject.TYPE_STRING)
        tree_view = gtk.TreeView(model)
        scrolled_window.add_with_viewport (tree_view)
        tree_view.show()

        # Add some messages to the window
        for i in range(10):
            msg = "Message #%d" % i
            iter = model.append()
            model.set(iter, 0, msg)

        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Messages", cell, text=0)
        tree_view.append_column(column)

        return scrolled_window
   
    # Add some text to our text widget - this is a callback that is invoked
    # when our window is realized. We could also force our window to be
    # realized with GtkWidget.realize, but it would have to be part of a
    # hierarchy first
    def insert_text(self, buffer):
        iter = buffer.get_iter_at_offset(0)
        buffer.insert(iter,
                      "From: pathfinder@nasa.gov\n"
                      "To: mom@nasa.gov\n"
                      "Subject: Made it!\n"
                      "\n"
                      "We just got in this morning. The weather has been\n"
                      "great - clear but cold, and there are lots of fun sights.\n"
                      "Sojourner says hi. See you soon.\n"
                      " -Path\n")
   
    # Create a scrolled text area that displays a "message"
    def create_text(self):
        view = gtk.TextView()
        buffer = view.get_buffer()
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolled_window.add(view)
        self.insert_text(buffer)
        scrolled_window.show_all()
        return scrolled_window
   
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Paned Windows")
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_border_width(10)
        window.set_size_request(450, 400)

        # create a vpaned widget and add it to our toplevel window
        vpaned = gtk.VPaned()
        window.add(vpaned)
        vpaned.show()

        # Now create the contents of the two halves of the window
        list = self.create_list()
        vpaned.add1(list)
        list.show()

        text = self.create_text()
        vpaned.add2(text)
        text.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    PanedExample()
    main()
