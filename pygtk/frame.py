#!/usr/bin/env python
#
# [SNIPPET_NAME: Frame]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a Frame widget]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Frames.html]

# example frame.py

import pygtk
pygtk.require('2.0')
import gtk

class FrameExample:
    def __init__(self):
        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Frame Example")

        # Here we connect the "destroy" event to a signal handler 
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_size_request(300, 300)

        # Sets the border width of the window.
        window.set_border_width(10)

        # Create a Frame
        frame = gtk.Frame()
        window.add(frame)

        # Set the frame's label
        frame.set_label("GTK Frame Widget")

        # Align the label at the right of the frame
        frame.set_label_align(1.0, 0.0)

        # Set the style of the frame
        frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
        frame.show()
  
        # Display the window
        window.show()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    FrameExample()
    main()
