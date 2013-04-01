#!/usr/bin/env python
#
# [SNIPPET_NAME: Button Box]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a button box]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-ButtonBoxes.html, http://www.pygtk.org/docs/pygtk/class-gtkbuttonbox.html, ]

# example buttonbox.py

import pygtk
pygtk.require('2.0')
import gtk

class ButtonBoxExample:
    # Create a Button Box with the specified parameters
    def create_bbox(self, horizontal, title, spacing, layout):
        frame = gtk.Frame(title)

        if horizontal:
            bbox = gtk.HButtonBox()
        else:
            bbox = gtk.VButtonBox()

        bbox.set_border_width(5)
        frame.add(bbox)

        # Set the appearance of the Button Box
        bbox.set_layout(layout)
        bbox.set_spacing(spacing)

        button = gtk.Button(stock=gtk.STOCK_OK)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_CANCEL)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_HELP)
        bbox.add(button)

        return frame

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Button Boxes")

        window.connect("destroy", lambda x: gtk.main_quit())

        window.set_border_width(10)

        main_vbox = gtk.VBox(False, 0)
        window.add(main_vbox)

        frame_horz = gtk.Frame("Horizontal Button Boxes")
        main_vbox.pack_start(frame_horz, True, True, 10)

        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(10)
        frame_horz.add(vbox)

        vbox.pack_start(self.create_bbox(True, "Spread (spacing 40)",
                                         40, gtk.BUTTONBOX_SPREAD),
                        True, True, 0)

        vbox.pack_start(self.create_bbox(True, "Edge (spacing 30)",
                                         30, gtk.BUTTONBOX_EDGE),
                        True, True, 5)

        vbox.pack_start(self.create_bbox(True, "Start (spacing 20)",
                                         20, gtk.BUTTONBOX_START),
                        True, True, 5)

        vbox.pack_start(self.create_bbox(True, "End (spacing 10)",
                                         10, gtk.BUTTONBOX_END),
                        True, True, 5)

        frame_vert = gtk.Frame("Vertical Button Boxes")
        main_vbox.pack_start(frame_vert, True, True, 10)

        hbox = gtk.HBox(False, 0)
        hbox.set_border_width(10)
        frame_vert.add(hbox)

        hbox.pack_start(self.create_bbox(False, "Spread (spacing 5)",
                                         5, gtk.BUTTONBOX_SPREAD),
                        True, True, 0)

        hbox.pack_start(self.create_bbox(False, "Edge (spacing 30)",
                                         30, gtk.BUTTONBOX_EDGE),
                        True, True, 5)

        hbox.pack_start(self.create_bbox(False, "Start (spacing 20)",
                                         20, gtk.BUTTONBOX_START),
                        True, True, 5)

        hbox.pack_start(self.create_bbox(False, "End (spacing 20)",
                                         20, gtk.BUTTONBOX_END),
                        True, True, 5)

        window.show_all()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    ButtonBoxExample()
    main()
