#!/usr/bin/env python
#
# [SNIPPET_NAME: Get Selection]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Get a selection]

# example getselection.py

import pygtk
pygtk.require('2.0')
import gtk

class GetSelectionExample:
    # Signal handler invoked when user clicks on the
    # "Get String Target" button
    def get_stringtarget(self, widget):
        # And request the "STRING" target for the primary selection
        ret = widget.selection_convert("PRIMARY", "STRING")
        return

    # Signal handler invoked when user clicks on the "Get Targets" button
    def get_targets(self, widget):
        # And request the "TARGETS" target for the primary selection
        ret = widget.selection_convert("PRIMARY", "TARGETS")
        return

    # Signal handler called when the selections owner returns the data
    def selection_received(self, widget, selection_data, data):
        # Make sure we got the data in the expected form
        if str(selection_data.type) == "STRING":
            # Print out the string we received
            print "STRING TARGET: %s" % selection_data.get_text()

        elif str(selection_data.type) == "ATOM":
            # Print out the target list we received
            targets = selection_data.get_targets()
            for target in targets:
                name = str(target)
                if name != None:
                    print "%s" % name
                else:
                    print "(bad target)"
        else:
            print "Selection was not returned as \"STRING\" or \"ATOM\"!"

        return False
  

    def __init__(self):
        # Create the toplevel window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Get Selection")
        window.set_border_width(10)
        window.connect("destroy", lambda w: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # Create a button the user can click to get the string target
        button = gtk.Button("Get String Target")
        eventbox = gtk.EventBox()
        eventbox.add(button)
        button.connect_object("clicked", self.get_stringtarget, eventbox)
        eventbox.connect("selection_received", self.selection_received)
        vbox.pack_start(eventbox)
        eventbox.show()
        button.show()

        # Create a button the user can click to get targets
        button = gtk.Button("Get Targets")
        eventbox = gtk.EventBox()
        eventbox.add(button)
        button.connect_object("clicked", self.get_targets, eventbox)
        eventbox.connect("selection_received", self.selection_received)
        vbox.pack_start(eventbox)
        eventbox.show()
        button.show()

        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    GetSelectionExample()
    main()
