#!/usr/bin/env python
#
# [SNIPPET_NAME: Desktop Widget]
# [SNIPPET_CATEGORIES: PyGTK, Cairo]
# [SNIPPET_DESCRIPTION: Standalone desktop widget with transparent background]
# [SNIPPET_AUTHOR: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>]
# [SNIPPET_LICENSE: GPL]

# For more information, see:
#   http://bloc.eurion.net/archives/2009/standalone-pygtk-desktop-widgets/

import gtk
import cairo

def transparent_expose(widget, event):
    """ Make the given widget transparent. """
    cr = widget.window.cairo_create()
    cr.set_operator(cairo.OPERATOR_CLEAR)
    region = gtk.gdk.region_rectangle(event.area)
    cr.region(region)
    cr.fill()
    return False

class DesktopWindow(gtk.Window):
    """ A transparent and borderless window, fixed on the desktop."""
    
    # Based upon the composited window example from:
    # http://www.pygtk.org/docs/pygtk/class-gdkwindow.html
    
    def __init__(self, *args):
        
        gtk.Window.__init__(self, *args)
        
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
        self.set_keep_below(True)
        self.set_decorated(False)
        self.stick()
        
        screen = self.get_screen()
        rgba = screen.get_rgba_colormap()
        self.set_colormap(rgba)
        self.set_app_paintable(True)
        self.connect("expose-event", transparent_expose)

class QuoteWidget:
    """ An example widget, which shows a quote embedded into your desktop."""
    
    def __init__(self):
        
        self.window = DesktopWindow()
        self.window.move(500, 100)
        
        self.box = gtk.HBox()
        self.window.add(self.box)
        
        self.label = gtk.Label()
        self.box.pack_start(self.label, expand=True)
        
        quote = "If they give you ruled paper write the other way."
        author = "Juan Ramon Jimenez"
        self.label.set_text("%s\n\t\t-- %s" % (quote, author))
        
        self.window.show_all()

if __name__ == "__main__":
    print "Look at your desktop! :)"
    instance = QuoteWidget()
    gtk.main()
