#!/usr/bin/env python
#
# [SNIPPET_NAME: Adding values to GConf]
# [SNIPPET_CATEGORIES: gconf, PyGTK]
# [SNIPPET_DESCRIPTION: Using GConf]
# [SNIPPET_AUTHOR: Travis Nicholl <uninja@enigma9.org>]
# [SNIPPET_LICENSE: GPL]

# example gconf-snippet.py

import sys

import pygtk
pygtk.require('2.0')
import gtk

try:
    import gconf
except:
    error = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, 'You need to install the python bindings for gconf')
    error.run()
    sys.exit(1)

ROOT_DIR = '/apps/acire/gconf-snippet'
NAME_KEY = ROOT_DIR + '/name'
AGE_KEY = ROOT_DIR + '/age'
FAN_KEY = ROOT_DIR + '/fan'

class GConfSnippet:

    def __init__(self):

        # Get GConf client:
        self.gconf_client = gconf.client_get_default()

        # Add the root directory to the list of directories that our GConf
        # client will watch for changes:
        self.gconf_client.add_dir(ROOT_DIR, gconf.CLIENT_PRELOAD_NONE)

        # Assign a callback function for when changes are made to keys in
        # the root directory namespace:
        self.gconf_client.notify_add(ROOT_DIR, self.prefs_changed_callback)

        # Create toplevel window, set attributes:
        self.window = gtk.Window()
        self.window.connect('destroy', lambda w: gtk.main_quit())
        self.window.set_border_width(9)
        self.window.set_title('GConf Snippet')

        # Create and add main layout box:
        table = gtk.Table(3, 2, True)
        self.window.add(table)

        # Create/add labels:
        label = gtk.Label('Name:')
        table.attach(label, 0, 1, 0, 1)

        label = gtk.Label('Age:')
        table.attach(label, 0, 1, 1, 2)

        # Create/add checkbutton:
        self.ubuntu_fan_button = gtk.CheckButton('Ubuntu fan')
        self.ubuntu_fan_button.set_active(self.gconf_client.get_bool(FAN_KEY) or False)
        self.ubuntu_fan_button.connect('toggled', self.check_button_callback)
        table.attach(self.ubuntu_fan_button, 0, 1, 2, 3)

        # Create/add entries:
        self.name_entry = gtk.Entry()
        self.name_entry.set_text(self.gconf_client.get_string(NAME_KEY) or "")
        self.name_entry.connect('changed', self.entry_changed_callback, 'name')
        table.attach(self.name_entry, 1, 2, 0, 1)

        self.age_entry = gtk.Entry()
        self.age_entry.set_text(self.gconf_client.get_string(AGE_KEY) or "")
        self.age_entry.connect('changed', self.entry_changed_callback, 'age')
        table.attach(self.age_entry, 1, 2, 1, 2)

        # Show all widgets:
        self.window.show_all()


    def check_button_callback(self, button):
        """
        This is the callback function that is called when the
        gtk.CheckButton is toggled.
        """
        self.gconf_client.set_bool(FAN_KEY, button.get_active())


    def entry_changed_callback(self, entry, pref_name):
        """
        This is the callback function that is called when either of the
        gtk.Entry widgets' text changes.
        """
        self.gconf_client.set_string(ROOT_DIR + '/%s' % pref_name, entry.get_text())


    def prefs_changed_callback(self, client, timestamp, entry, *extra):
        """
        This is the callback function that is called when the keys in our
        namespace change (such as editing them with gconf-editor).
        """
        key = entry.get_key()

        if key == NAME_KEY:
            self.name_entry.set_text(entry.get_value().get_string())
        elif key == AGE_KEY:
            self.age_entry.set_text(entry.get_value().get_string())
        elif key == FAN_KEY:
            self.ubuntu_fan_button.set_active(entry.get_value().get_bool())
        else:
            print 'Error: Unknown key changed.'


if __name__ == '__main__':
    ge = GConfSnippet()
    gtk.main()
