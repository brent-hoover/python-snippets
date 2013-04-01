#!/usr/bin/env python
#
# [SNIPPET_NAME: Set Selection]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Dealing with selections]

# example setselection.py

import pygtk
pygtk.require('2.0')
import gtk
import time

class SetSelectionExample:
    # Callback when the user toggles the selection
    def selection_toggled(self, widget, window):
        if widget.get_active():
            self.have_selection = window.selection_owner_set("PRIMARY")
            # if claiming the selection failed, we return the button to
            # the out state
            if not self.have_selection:
                widget.set_active(False)
        else:
            if self.have_selection:
                # Not possible to release the selection in PyGTK
                # just mark that we don't have it
                self.have_selection = False
        return

    # Called when another application claims the selection
    def selection_clear(self, widget, event):
        self.have_selection = False
        widget.set_active(False)
        return True

    # Supplies the current time as the selection.
    def selection_handle(self, widget, selection_data, info, time_stamp):
        current_time = time.time()
        timestr = time.asctime(time.localtime(current_time))

        # When we return a single string, it should not be null terminated.
        # That will be done for us
        selection_data.set_text(timestr, len(timestr))
        return

    def __init__(self):
        self.have_selection = False
        # Create the toplevel window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Set Selection")
        window.set_border_width(10)
        window.connect("destroy", lambda w: gtk.main_quit())
        self.window = window
        # Create an eventbox to hold the button since it no longer has
        # a GdkWindow
        eventbox = gtk.EventBox()
        eventbox.show()
        window.add(eventbox)
        
        # Create a toggle button to act as the selection
        selection_button = gtk.ToggleButton("Claim Selection")
        eventbox.add(selection_button)

        selection_button.connect("toggled", self.selection_toggled, eventbox)
        eventbox.connect_object("selection_clear_event", self.selection_clear,
                                selection_button)

        eventbox.selection_add_target("PRIMARY", "STRING", 1)
        eventbox.selection_add_target("PRIMARY", "COMPOUND_TEXT", 1)
        eventbox.connect("selection_get", self.selection_handle)
        selection_button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    SetSelectionExample()
    main()
