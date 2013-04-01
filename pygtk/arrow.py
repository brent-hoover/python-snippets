#!/usr/bin/env python
#
# [SNIPPET_NAME: Arrow]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Demonstrates how to create arrow buttons.]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkarrow.html, http://www.pygtk.org/pygtk2tutorial/sec-TooltipsObject.html]

import pygtk
pygtk.require('2.0')
import gtk

# Create an Arrow widget with the specified parameters
# and pack it into a button
def create_arrow_button(arrow_type, shadow_type):
    button = gtk.Button();
    arrow = gtk.Arrow(arrow_type, shadow_type);
    button.add(arrow)
    button.show()
    arrow.show()
    return button

class Arrows:
    def __init__(self):
        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        window.set_title("Arrow Buttons")

        # It's a good idea to do this for all windows.
        window.connect("destroy", lambda x: gtk.main_quit())

        # Sets the border width of the window.
        window.set_border_width(10)

        # Create a box to hold the arrows/buttons
        box = gtk.HBox(False, 0)
        box.set_border_width(2)
        window.add(box)

        # Pack and show all our widgets
        box.show()

        button = create_arrow_button(gtk.ARROW_UP, gtk.SHADOW_IN)
        box.pack_start(button, False, False, 3)

        button = create_arrow_button(gtk.ARROW_DOWN, gtk.SHADOW_OUT)
        box.pack_start(button, False, False, 3)
  
        button = create_arrow_button(gtk.ARROW_LEFT, gtk.SHADOW_ETCHED_IN)
        box.pack_start(button, False, False, 3)
  
        button = create_arrow_button(gtk.ARROW_RIGHT, gtk.SHADOW_ETCHED_OUT)
        box.pack_start(button, False, False, 3)
  
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Arrows()
    main()
