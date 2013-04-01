#!/usr/bin/env python
#
# [SNIPPET_NAME: Drag and Drop]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Add drag and drop support to your application]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-DragAndDrop.html]

# example dragndrop.py

import pygtk
pygtk.require('2.0')
import gtk
import string, time

import gtkxpm

class DragNDropExample:
    HEIGHT = 600
    WIDTH = 600
    TARGET_TYPE_TEXT = 80
    TARGET_TYPE_PIXMAP = 81
    fromImage = [ ( "text/plain", 0, TARGET_TYPE_TEXT ),
              ( "image/x-xpixmap", 0, TARGET_TYPE_PIXMAP ) ]
    toButton = [ ( "text/plain", 0, TARGET_TYPE_TEXT ) ]
    toCanvas = [ ( "image/x-xpixmap", 0, TARGET_TYPE_PIXMAP ) ]

    def layout_resize(self, widget, event):
        x, y, width, height = widget.get_allocation()
        if width > self.lwidth or height > self.lheight:
            self.lwidth = max(width, self.lwidth)
            self.lheight = max(height, self.lheight)
            widget.set_size(self.lwidth, self.lheight)

    def makeLayout(self):
        self.lwidth = self.WIDTH
        self.lheight = self.HEIGHT
        box = gtk.VBox(False,0)
        box.show()
        table = gtk.Table(2, 2, False)
        table.show()
        box.pack_start(table, True, True, 0)
        layout = gtk.Layout()
        self.layout = layout
        layout.set_size(self.lwidth, self.lheight)
        layout.connect("size-allocate", self.layout_resize)
        layout.show()
        table.attach(layout, 0, 1, 0, 1, gtk.FILL|gtk.EXPAND,
                     gtk.FILL|gtk.EXPAND, 0, 0)
        # create the scrollbars and pack into the table
        vScrollbar = gtk.VScrollbar(None)
        vScrollbar.show()
        table.attach(vScrollbar, 1, 2, 0, 1, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK, 0, 0)
        hScrollbar = gtk.HScrollbar(None)
        hScrollbar.show()
        table.attach(hScrollbar, 0, 1, 1, 2, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK,
                     0, 0)
        # tell the scrollbars to use the layout widget's adjustments
        vAdjust = layout.get_vadjustment()
        vScrollbar.set_adjustment(vAdjust)
        hAdjust = layout.get_hadjustment()
        hScrollbar.set_adjustment(hAdjust)
        layout.connect("drag_data_received", self.receiveCallback)
        layout.drag_dest_set(gtk.DEST_DEFAULT_MOTION |
                                  gtk.DEST_DEFAULT_HIGHLIGHT |
                                  gtk.DEST_DEFAULT_DROP,
                                  self.toCanvas, gtk.gdk.ACTION_COPY)
        self.addImage(gtkxpm.gtk_xpm, 0, 0)
        button = gtk.Button("Text Target")
        button.show()
        button.connect("drag_data_received", self.receiveCallback)
        button.drag_dest_set(gtk.DEST_DEFAULT_MOTION |
                             gtk.DEST_DEFAULT_HIGHLIGHT |
                             gtk.DEST_DEFAULT_DROP,
                             self.toButton, gtk.gdk.ACTION_COPY)
        box.pack_start(button, False, False, 0)
        return box

    def addImage(self, xpm, xd, yd):
        hadj = self.layout.get_hadjustment()
        vadj = self.layout.get_vadjustment()
        style = self.window.get_style()
        pixmap, mask = gtk.gdk.pixmap_create_from_xpm_d(
            self.window.window, style.bg[gtk.STATE_NORMAL], xpm)
        image = gtk.Image()
        image.set_from_pixmap(pixmap, mask)
        button = gtk.Button()
        button.add(image)
        button.connect("drag_data_get", self.sendCallback)
        button.drag_source_set(gtk.gdk.BUTTON1_MASK, self.fromImage,
                               gtk.gdk.ACTION_COPY)
        button.show_all()
        # have to adjust for the scrolling of the layout - event location
        # is relative to the viewable not the layout size
        self.layout.put(button, int(xd+hadj.value), int(yd+vadj.value))
        return

    def sendCallback(self, widget, context, selection, targetType, eventTime):
        if targetType == self.TARGET_TYPE_TEXT:
            now = time.time()
            str = time.ctime(now)
            selection.set(selection.target, 8, str)
        elif targetType == self.TARGET_TYPE_PIXMAP:
            selection.set(selection.target, 8,
                          string.join(gtkxpm.gtk_xpm, '\n'))

    def receiveCallback(self, widget, context, x, y, selection, targetType,
                        time):
        if targetType == self.TARGET_TYPE_TEXT:
            label = widget.get_children()[0]
            label.set_text(selection.data)
        elif targetType == self.TARGET_TYPE_PIXMAP:
            self.addImage(string.split(selection.data, '\n'), x, y)

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(300, 300)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.show()
        layout = self.makeLayout()
        self.window.add(layout)

def main():
    gtk.main()

if __name__ == "__main__":
    DragNDropExample()
    main()
