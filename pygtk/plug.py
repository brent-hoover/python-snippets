#!/usr/bin/python
#
# [SNIPPET_NAME: Plug]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using gtk.Plug]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-PlugsAndSockets.html, http://www.pygtk.org/docs/pygtk/class-gtkplug.html]

import pygtk
pygtk.require('2.0')
import gtk,sys

Wid = 0L
if len(sys.argv) == 2:
    Wid = long(sys.argv[1])

plug = gtk.Plug(Wid)
print "Plug ID=", plug.get_id()

def embed_event(widget):
    print "I (", widget, ") have just been embedded!"

plug.connect("embedded", embed_event)

entry = gtk.Entry()
entry.set_text("hello")
def entry_point(widget):
    print "You've changed my text to '%s'" % widget.get_text()

entry.connect("changed", entry_point)
plug.connect("destroy", lambda w: gtk.main_quit())

plug.add(entry)
plug.show_all()


gtk.main()
