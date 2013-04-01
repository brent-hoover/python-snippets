#!/usr/bin/env python
#
# [SNIPPET_NAME: Builder]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a Simple GUI from Glade XML file with Builder]
# [SNIPPET_AUTHOR: Andre "Osku" Schmidt <andre.osku.schmidt@osku.de>]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkbuilder.html]
# [SNIPPET_LICENSE: GPL]

import sys
import gtk
  
class BuilderExample:

    # Signal connection is linked in the glade XML file
    def on_window_destroy(self, widget, data=None):
        gtk.main_quit()

    # Signal connection is linked in the glade XML file
    def on_button1_clicked(self, widget, data=None):
        text = self.entry1.get_text()
        self.label1.set_text(text)
     
    def __init__(self):
        # Create a new Builder object
        builder = gtk.Builder()
        # Add the UI objects (widgets) from the Glade XML file
        builder.add_from_file("builder.ui")
        
        # Get objects (widgets) from the Builder
        self.window = builder.get_object("window")
        self.entry1 = builder.get_object("entry1");
        self.label1 = builder.get_object("label1");
        # Connect all singals to methods in this class
        builder.connect_signals(self)
        # Show the window and all its children
        self.window.show_all()

def main():
    gtk.main()
    return
    
if __name__ == "__main__":
    BuilderExample()
    gtk.main()
