#!/usr/bin/env python

# [SNIPPET_NAME: Embed a VTE terminal]
# [SNIPPET_CATEGORIES: Python VTE]
# [SNIPPET_DESCRIPTION: Embed a VTE terminal in your application]

import sys

try:
    import gtk
except:
    print >> sys.stderr, "You need to install the python gtk bindings"
    sys.exit(1)

# import vte
try:
    import vte
except:
    error = gtk.MessageDialog (None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
        'You need to install python bindings for libvte')
    error.run()
    sys.exit (1)

if __name__ == '__main__':
    # create the terminal
    v = vte.Terminal()
    v.connect ("child-exited", lambda term: gtk.main_quit())

    # fork_command() will run a command, in this case it shows a prompt
    v.fork_command()

    # create a window and add the VTE
    window = gtk.Window()
    window.add(v)
    window.connect('delete-event', lambda window, event: gtk.main_quit())

    # you need to show the VTE
    window.show_all()

    # Finally, run the application
    gtk.main()

