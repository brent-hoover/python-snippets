#!/usr/bin/env python
#
# [SNIPPET_NAME: Pixmap]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Adding pixmaps to your application]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtktutorial/sec-pixmaps.html, http://www.pygtk.org/pygtk2tutorial/sec-DrawingAreaWidgetAndDrawing.html, http://www.pygtk.org/docs/pygtk/class-gdkpixmap.html]

# example pixmap.py

import pygtk
pygtk.require('2.0')
import gtk

# XPM data of Open-File icon
xpm_data = [
"16 16 3 1",
"       c None",
".      c #000000000000",
"X      c #FFFFFFFFFFFF",
"                ",
"   ......       ",
"   .XXX.X.      ",
"   .XXX.XX.     ",
"   .XXX.XXX.    ",
"   .XXX.....    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .........    ",
"                ",
"                "
]

class PixmapExample:
    # when invoked (via signal delete_event), terminates the application.
    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    # is invoked when the button is clicked.  It just prints a message.
    def button_clicked(self, widget, data=None):
        print "button clicked"

    def __init__(self):
        # create the main window, and attach delete_event signal to terminating
        # the application
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.close_application)
        window.set_border_width(10)
        window.show()

        # now for the pixmap from XPM data
        pixmap, mask = gtk.gdk.pixmap_create_from_xpm_d(window.window,
                                                        None,
                                                        xpm_data)

        # an image widget to contain the pixmap
        image = gtk.Image()
        image.set_from_pixmap(pixmap, mask)
        image.show()

        # a button to contain the image widget
        button = gtk.Button()
        button.add(image)
        window.add(button)
        button.show()

        button.connect("clicked", self.button_clicked)

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    PixmapExample()
    main()
