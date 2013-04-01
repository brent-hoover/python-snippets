#!/usr/bin/env python
#
# [SNIPPET_NAME: Buttons]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a push button]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkbutton.html]

# example-start buttons buttons.py

import pygtk
pygtk.require('2.0')
import gtk

# Create a new hbox with an image and a label packed into it
# and return the box.

def xpm_label_box(parent, xpm_filename, label_text):
    # Create box for xpm and label
    box1 = gtk.HBox(False, 0)
    box1.set_border_width(2)

    # Now on to the image stuff
    image = gtk.Image()
    image.set_from_file(xpm_filename)

    # Create a label for the button
    label = gtk.Label(label_text)

    # Pack the pixmap and label into the box
    box1.pack_start(image, False, False, 3)
    box1.pack_start(label, False, False, 3)

    image.show()
    label.show()
    return box1

class Buttons:
    # Our usual callback method
    def callback(self, widget, data=None):
        print "Hello again - %s was pressed" % data

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Image'd Buttons!")

        # It's a good idea to do this for all windows.
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        # Sets the border width of the window.
        self.window.set_border_width(10)

        # Create a new button
        button = gtk.Button()

        # Connect the "clicked" signal of the button to our callback
        button.connect("clicked", self.callback, "cool button")

        # This calls our box creating function
        box1 = xpm_label_box(self.window, "info.xpm", "cool button")

        # Pack and show all our widgets
        button.add(box1)

        box1.show()
        button.show()

        self.window.add(button)
        self.window.show()

def main():
    gtk.main()
    return 0     

if __name__ == "__main__":
    Buttons()
    main()
