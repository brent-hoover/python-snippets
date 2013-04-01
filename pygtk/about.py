#!/usr/bin/env python
#
# [SNIPPET_NAME: About Dialog]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create an AboutDialog]
# [SNIPPET_AUTHOR: Jon Staley]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkaboutdialog.html]
# [SNIPPET_LICENSE: MIT]

# example about.py

import pygtk
pygtk.require('2.0')
import gtk

class AboutDialogExample:

    def __init__(self):
        # Create base window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Connect the destroy signal to gtk.main_quit ensuring the
        # application closes gracefully
        self.window.connect("destroy", gtk.main_quit, None)

        # Create simple button
        self.button = gtk.Button("About Dialog")

        # Connect button to the show_about method
        self.button.connect("clicked", self.show_about, None)

        # Add button to the window and show both
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

    def show_about(self, widget, data):
        # The AboutDialog has good helper methods which
        # setup the dialog and add the content ensuring all
        # about dialog are consistant.  Below is a small example

        # Create AboutDialog object
        dialog = gtk.AboutDialog()

        # Add the application name to the dialog
        dialog.set_name('Example About Dialog')

        # Set the application version
        dialog.set_version('0.1')

        # Pass a list of authors.  This is then connected to the 'Credits'
        # button.  When clicked the buttons opens a new window showing
        # each author on their own line.
        dialog.set_authors(['Jon Staley', 'Example'])

        # Add a short comment about the application, this appears below the application
        # name in the dialog
        dialog.set_comments('A simple example of an about dialog.')

        # Add license information, this is connected to the 'License' button
        # and is displayed in a new window.
        dialog.set_license('Distributed under the MIT license.\nhttp://www.opensource.org/licenses/mit-license.php')

        # Show the dialog
        dialog.run()

        # The destroy method must be called otherwise the 'Close' button will
        # not work.
        dialog.destroy()

    def hide_dialog(self, widget, data):
        widget.hide()

if __name__ == "__main__":
    about = AboutDialogExample()
    about.main()
