#!/usr/local/env python
#
# [SNIPPET_NAME: Drag Open File]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Get the path of a file dragged onto the application]
# [SNIPPET_AUTHOR: Rich Jones <rich@anomos.info>]
# [SNIPPET_LICENSE: Public Domain]

import pygtk
pygtk.require('2.0')
import gtk
import urllib
import os

def on_drag_data_received(widget, context, x, y, selection, target_type, timestamp):
    uri = selection.data.strip('\r\n\x00')
    uri_splitted = uri.split() # we may have more than one file dropped
    for uri in uri_splitted:
        path = get_file_path_from_dnd_dropped_uri(uri)
        if os.path.isfile(path): # is it file?
            # your_open_file_function(path)
            # You might also want to look at the File Chooser snippet
            l.set_text("File: %s"%path)
            # If you actually want to read the data in the file, use
            # data = file(path).read()

def get_file_path_from_dnd_dropped_uri(uri):
    #get the path to file
    path = ""
    if uri.startswith('file:\\\\\\'): # windows
        path = uri[8:] # 8 is len('file:///')
    elif uri.startswith('file://'): # nautilus, rox
        path = uri[7:] # 7 is len('file://')
    elif uri.startswith('file:'): # xffm
        path = uri[5:] # 5 is len('file:')

    path = urllib.url2pathname(path) # escape special chars
    path = path.strip('\r\n\x00') # remove \r\n and NULL
    return path

w = gtk.Window()
w.set_size_request(200, 150)

#This is the important bit
TARGET_TYPE_URI_LIST = 80
dnd_list = [ ( 'text/uri-list', 0, TARGET_TYPE_URI_LIST ) ]
w.connect('drag_data_received', on_drag_data_received)
w.drag_dest_set( gtk.DEST_DEFAULT_MOTION |
                  gtk.DEST_DEFAULT_HIGHLIGHT | gtk.DEST_DEFAULT_DROP,
                  dnd_list, gtk.gdk.ACTION_COPY)

w.connect('destroy', lambda w: gtk.main_quit())
l = gtk.Label("Drag something here!")
w.add(l)
w.show_all()

gtk.main()
