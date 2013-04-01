#!/usr/bin/env python
#
# [SNIPPET_NAME: Aspect Frame]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create and use an aspect frame with gtk.AspectFrame]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-AspectFrames.html, http://www.pygtk.org/docs/pygtk/class-gtkaspectframe.html]

# example aspectframe.py

import pygtk
pygtk.require('2.0')
import gtk

class AspectFrameExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL);
        window.set_title("Aspect Frame")
        window.connect("destroy", lambda x: gtk.main_quit())
        window.set_border_width(10)

        # Create an aspect_frame and add it to our toplevel window
        aspect_frame = gtk.AspectFrame("2x1", # label
                                       0.5, # center x
                                       0.5, # center y
                                       2, # xsize/ysize = 2
                                       False) # ignore child's aspect
        window.add(aspect_frame)
        aspect_frame.show()

        # Now add a child widget to the aspect frame
        drawing_area = gtk.DrawingArea()

        # Ask for a 200x200 window, but the AspectFrame will give us a 200x100
        # window since we are forcing a 2x1 aspect ratio
        drawing_area.set_size_request(200, 200)
        aspect_frame.add(drawing_area)
        drawing_area.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    AspectFrameExample()
    main()
