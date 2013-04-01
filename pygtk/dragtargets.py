#!/usr/local/env python
#
# [SNIPPET_NAME: Drag Targets]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create drag and drop drag targets]

import pygtk
pygtk.require('2.0')
import gtk

def motion_cb(wid, context, x, y, time):
    context.drag_status(gtk.gdk.ACTION_COPY, time)
    return True

def drop_cb(wid, context, x, y, time):
    l.set_text('\n'.join([str(t) for t in context.targets]))
    context.finish(True, False, time)
    return True

w = gtk.Window()
w.set_size_request(200, 150)
w.drag_dest_set(0, [], 0)
w.connect('drag_motion', motion_cb)
w.connect('drag_drop', drop_cb)
w.connect('destroy', lambda w: gtk.main_quit())
l = gtk.Label()
w.add(l)
w.show_all()

gtk.main()
