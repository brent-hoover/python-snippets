#!/usr/bin/python
#
# [SNIPPET_NAME: Socket]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a socket]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-PlugsAndSockets.html, http://www.pygtk.org/docs/pygtk/class-gtksocket.html]

import string

import pygtk
pygtk.require('2.0')
import gtk,sys

window = gtk.Window()
window.show()

socket = gtk.Socket()
socket.show()
window.add(socket)

print "Socket ID=", socket.get_id()
window.connect("destroy", lambda w: gtk.main_quit())

def plugged_event(widget):
    print "I (", widget, ") have just had a plug inserted!"

socket.connect("plug-added", plugged_event)

if len(sys.argv) == 2:
    socket.add_id(long(sys.argv[1]))

gtk.main()
