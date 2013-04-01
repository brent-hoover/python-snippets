#!/usr/bin/env python
#
# [SNIPPET_NAME: Simple Action]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Creating a simple action]

import pygtk
pygtk.require('2.0')
import gtk

class SimpleAction:
    def __init__(self):
        # Create the toplevel window
        window = gtk.Window()
        window.set_size_request(70, 30)
        window.connect('destroy', lambda w: gtk.main_quit())

        # Create an accelerator group
        accelgroup = gtk.AccelGroup()
        # Add the accelerator group to the toplevel window
        window.add_accel_group(accelgroup)

        # Create an action for quitting the program using a stock item
        action = gtk.Action('Quit', None, None, gtk.STOCK_QUIT)
        # Connect a callback to the action
        action.connect('activate', self.quit_cb)

        # Create an ActionGroup named SimpleAction
        actiongroup = gtk.ActionGroup('SimpleAction')
        # Add the action to the actiongroup with an accelerator
        # None means use the stock item accelerator
        actiongroup.add_action_with_accel(action, None)

        # Have the action use accelgroup
        action.set_accel_group(accelgroup)

        # Connect the accelerator to the action
        action.connect_accelerator()

        # Create the button to use as the action proxy widget
        quitbutton = gtk.Button()
        # add it to the window
        window.add(quitbutton)

        # Connect the action to its proxy widget
        action.connect_proxy(quitbutton)

        window.show_all()
        return

    def quit_cb(self, b):
        print 'Quitting program'
        gtk.main_quit()

if __name__ == '__main__':
    sa = SimpleAction()
    gtk.main()
