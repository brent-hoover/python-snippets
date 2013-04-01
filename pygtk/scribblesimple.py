#!/usr/bin/env python

# example scribblesimple.py

 # GTK - The GIMP Toolkit
 # Copyright (C) 1995-1997 Peter Mattis, Spencer Kimball and Josh MacDonald
 # Copyright (C) 2001-2004 John Finlay
 #
 # This library is free software; you can redistribute it and/or
 # modify it under the terms of the GNU Library General Public
 # License as published by the Free Software Foundation; either
 # version 2 of the License, or (at your option) any later version.
 #
 # This library is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 # Library General Public License for more details.
 #
 # You should have received a copy of the GNU Library General Public
 # License along with this library; if not, write to the
 # Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 # Boston, MA 02111-1307, USA.
#
# [SNIPPET_NAME: Scribble Simple]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: A simple scribbling example]

import pygtk
pygtk.require('2.0')
import gtk

# Backing pixmap for drawing area
pixmap = None

# Create a new backing pixmap of the appropriate size
def configure_event(widget, event):
    global pixmap

    x, y, width, height = widget.get_allocation()
    pixmap = gtk.gdk.Pixmap(widget.window, width, height)
    pixmap.draw_rectangle(widget.get_style().white_gc,
                          True, 0, 0, width, height)

    return True

# Redraw the screen from the backing pixmap
def expose_event(widget, event):
    x , y, width, height = event.area
    widget.window.draw_drawable(widget.get_style().fg_gc[gtk.STATE_NORMAL],
                                pixmap, x, y, x, y, width, height)
    return False

# Draw a rectangle on the screen
def draw_brush(widget, x, y):
    rect = (int(x-5), int(y-5), 10, 10)
    pixmap.draw_rectangle(widget.get_style().black_gc, True,
                          rect[0], rect[1], rect[2], rect[3])
    widget.queue_draw_area(rect[0], rect[1], rect[2], rect[3])

def button_press_event(widget, event):
    if event.button == 1 and pixmap != None:
        draw_brush(widget, event.x, event.y)
    return True

def motion_notify_event(widget, event):
    if event.is_hint:
        x, y, state = event.window.get_pointer()
    else:
        x = event.x
        y = event.y
        state = event.state
    
    if state & gtk.gdk.BUTTON1_MASK and pixmap != None:
        draw_brush(widget, x, y)
  
    return True

def main():
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_name ("Test Input")

    vbox = gtk.VBox(False, 0)
    window.add(vbox)
    vbox.show()

    window.connect("destroy", lambda w: gtk.main_quit())

    # Create the drawing area
    drawing_area = gtk.DrawingArea()
    drawing_area.set_size_request(200, 200)
    vbox.pack_start(drawing_area, True, True, 0)

    drawing_area.show()

    # Signals used to handle backing pixmap
    drawing_area.connect("expose_event", expose_event)
    drawing_area.connect("configure_event", configure_event)

    # Event signals
    drawing_area.connect("motion_notify_event", motion_notify_event)
    drawing_area.connect("button_press_event", button_press_event)

    drawing_area.set_events(gtk.gdk.EXPOSURE_MASK
                            | gtk.gdk.LEAVE_NOTIFY_MASK
                            | gtk.gdk.BUTTON_PRESS_MASK
                            | gtk.gdk.POINTER_MOTION_MASK
                            | gtk.gdk.POINTER_MOTION_HINT_MASK)

    # .. And a quit button
    button = gtk.Button("Quit")
    vbox.pack_start(button, False, False, 0)

    button.connect_object("clicked", lambda w: w.destroy(), window)
    button.show()

    window.show()

    gtk.main()

    return 0

if __name__ == "__main__":
    main()
