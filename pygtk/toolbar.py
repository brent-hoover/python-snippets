#!/usr/bin/env python
#
# [SNIPPET_NAME: Toolbar]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: How to add a toolbar]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Toolbar.html, http://www.pygtk.org/docs/pygtk/class-gtktoolbar.html]

# example toolbar.py

import pygtk
pygtk.require('2.0')
import gtk

class ToolbarExample:
    # This method is connected to the Close button or
    # closing the window from the WM
    def delete_event(self, widget, event=None):
        gtk.main_quit()
        return False

    # that's easy... when one of the buttons is toggled, we just
    # check which one is active and set the style of the toolbar
    # accordingly
    def radio_event(self, widget, toolbar):
        if self.text_button.get_active(): 
            toolbar.set_style(gtk.TOOLBAR_TEXT)
        elif self.icon_button.get_active():
            toolbar.set_style(gtk.TOOLBAR_ICONS)
        elif self.both_button.get_active():
            toolbar.set_style(gtk.TOOLBAR_BOTH)

    # even easier, just check given toggle button and enable/disable 
    # tooltips
    def toggle_event(self, widget, toolbar):
        toolbar.set_tooltips(widget.get_active())

    def __init__(self):
        # Here is our main window (a dialog) and a handle for the handlebox
        # Ok, we need a toolbar, an icon with a mask (one for all of 
        # the buttons) and an icon widget to put this icon in (but 
        # we'll create a separate widget for each button)
        # create a new window with a given title, and nice size
        dialog = gtk.Dialog()
        dialog.set_title("GTKToolbar Tutorial")
        dialog.set_size_request(450, 250)
        dialog.set_resizable(True)

        # typically we quit if someone tries to close us
        dialog.connect("delete_event", self.delete_event)

        # to make it nice we'll put the toolbar into the handle box, 
        # so that it can be detached from the main window
        handlebox = gtk.HandleBox()
        dialog.vbox.pack_start(handlebox, False, False, 5)

        # toolbar will be horizontal, with both icons and text, and
        # with 5pxl spaces between items and finally, 
        # we'll also put it into our handlebox
        toolbar = gtk.Toolbar()
        toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        toolbar.set_style(gtk.TOOLBAR_BOTH)
        toolbar.set_border_width(5)
        handlebox.add(toolbar)

        # our first item is <close> button
        iconw = gtk.Image() # icon widget
        iconw.set_from_file("gtk.xpm")
        close_button = toolbar.append_item(
            "Close",           # button label
            "Closes this app", # this button's tooltip
            "Private",         # tooltip private info
            iconw,             # icon widget
            self.delete_event) # a signal
        toolbar.append_space() # space after item

        # now, let's make our radio buttons group...
        iconw = gtk.Image() # icon widget
        iconw.set_from_file("gtk.xpm")
        icon_button = toolbar.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON, # type of element
            None,                          # widget
            "Icon",                        # label
            "Only icons in toolbar",       # tooltip
            "Private",                     # tooltip private string
            iconw,                         # icon
            self.radio_event,              # signal
            toolbar)                       # data for signal
        toolbar.append_space()
        self.icon_button = icon_button

        # following radio buttons refer to previous ones
        iconw = gtk.Image() # icon widget
        iconw.set_from_file("gtk.xpm")
        text_button = toolbar.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON,
            icon_button,
            "Text",
            "Only texts in toolbar",
            "Private",
            iconw,
            self.radio_event,
            toolbar)
        toolbar.append_space()
        self.text_button = text_button

        iconw = gtk.Image() # icon widget
        iconw.set_from_file("gtk.xpm")
        both_button = toolbar.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON,
            text_button,
            "Both",
            "Icons and text in toolbar",
            "Private",
            iconw,
            self.radio_event,
            toolbar)
        toolbar.append_space()
        self.both_button = both_button
        both_button.set_active(True)

        # here we have just a simple toggle button
        iconw = gtk.Image() # icon widget
        iconw.set_from_file("gtk.xpm")
        tooltips_button = toolbar.append_element(
            gtk.TOOLBAR_CHILD_TOGGLEBUTTON,
            None,
            "Tooltips",
            "Toolbar with or without tips",
            "Private",
            iconw,
            self.toggle_event,
            toolbar)
        toolbar.append_space()
        tooltips_button.set_active(True)

        # to pack a widget into toolbar, we only have to 
        # create it and append it with an appropriate tooltip
        entry = gtk.Entry()
        toolbar.append_widget(entry,  "This is just an entry", "Private")

        # well, it isn't created within the toolbar, so we must still show it
        entry.show()

        # that's it ! let's show everything.
        toolbar.show()
        handlebox.show()
        dialog.show()

def main():
    # rest in gtk_main and wait for the fun to begin!
    gtk.main()
    return 0

if __name__ == "__main__":
    ToolbarExample()
    main()
