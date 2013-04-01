#!/usr/bin/env python
#
# [SNIPPET_NAME: Event Box]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create an event box]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-ContainerWidgets.html, http://www.pygtk.org/docs/pygtk/class-gtkeventbox.html]

# example eventbox.py

import pygtk
pygtk.require('2.0')
import gtk

class EventBoxExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Event Box")
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_border_width(10)

        # Create an EventBox and add it to our toplevel window
        event_box = gtk.EventBox()
        window.add(event_box)
        event_box.show()

        # Create a long label
        label = gtk.Label("Click here to quit, quit, quit, quit, quit")
        event_box.add(label)
        label.show()

        # Clip it short.
        label.set_size_request(110, 20)

        # And bind an action to it
        event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        event_box.connect("button_press_event", lambda w,e: gtk.main_quit())

        # More things you need an X window for ...
        event_box.realize()
        event_box.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))

        # Set background color to green
        event_box.modify_bg(gtk.STATE_NORMAL,
                            event_box.get_colormap().alloc_color("green"))

        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    EventBoxExample()
    main()
