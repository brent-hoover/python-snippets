#!/usr/bin/env python
#
# [SNIPPET_NAME: Rulers]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using rulers]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtktutorial/sec-rulers.html, http://www.pygtk.org/docs/pygtk/class-gtkruler.html]

# example rulers.py

import pygtk
pygtk.require('2.0')
import gtk

class RulersExample:
    XSIZE = 400
    YSIZE = 400

    # This routine gets control when the close button is clicked
    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.close_application)
        window.set_border_width(10)

        # Create a table for placing the ruler and the drawing area
        table = gtk.Table(3, 2, False)
        window.add(table)

        area = gtk.DrawingArea()
        area.set_size_request(self.XSIZE, self.YSIZE)
        table.attach(area, 1, 2, 1, 2,
                     gtk.EXPAND|gtk.FILL, gtk.FILL, 0, 0 )
        area.set_events(gtk.gdk.POINTER_MOTION_MASK |
                        gtk.gdk.POINTER_MOTION_HINT_MASK )

        # The horizontal ruler goes on top. As the mouse moves across the
        # drawing area, a motion_notify_event is passed to the
        # appropriate event handler for the ruler.
        hrule = gtk.HRuler()
        hrule.set_metric(gtk.PIXELS)
        hrule.set_range(7, 13, 0, 20)
        def motion_notify(ruler, event):
            return ruler.emit("motion_notify_event", event)
        area.connect_object("motion_notify_event", motion_notify, hrule)
        table.attach(hrule, 1, 2, 0, 1,
                     gtk.EXPAND|gtk.SHRINK|gtk.FILL, gtk.FILL, 0, 0 )
    
        # The vertical ruler goes on the left. As the mouse moves across
        # the drawing area, a motion_notify_event is passed to the
        # appropriate event handler for the ruler.
        vrule = gtk.VRuler()
        vrule.set_metric(gtk.PIXELS)
        vrule.set_range(0, self.YSIZE, 10, self.YSIZE)
        area.connect_object("motion_notify_event", motion_notify, vrule)
        table.attach(vrule, 0, 1, 1, 2,
                     gtk.FILL, gtk.EXPAND|gtk.SHRINK|gtk.FILL, 0, 0 )

        # Now show everything
        area.show()
        hrule.show()
        vrule.show()
        table.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    RulersExample()
    main()
