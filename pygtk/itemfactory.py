#!/usr/bin/env python
#
# [SNIPPET_NAME: Item Factory]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using an item factory]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-ItemFactoryExample.html, http://www.pygtk.org/docs/pygtk/class-gtkitemfactory.html]

# example itemfactory.py

import pygtk
pygtk.require('2.0')
import gtk

class ItemFactoryExample:
    # Obligatory basic callback
    def print_hello(self, w, data):
        print "Hello, World!"

    # This is the ItemFactoryEntry structure used to generate new menus.
    # Item 1: The menu path. The letter after the underscore indicates an
    #         accelerator key once the menu is open.
    # Item 2: The accelerator key for the entry
    # Item 3: The callback.
    # Item 4: The callback action.  This changes the parameters with
    #         which the callback is called.  The default is 0.
    # Item 5: The item type, used to define what kind of an item it is.
    #       Here are the possible values:

    #       NULL               -> "<Item>"
    #       ""                 -> "<Item>"
    #       "<Title>"          -> create a title item
    #       "<Item>"           -> create a simple item
    #       "<CheckItem>"      -> create a check item
    #       "<ToggleItem>"     -> create a toggle item
    #       "<RadioItem>"      -> create a radio item
    #       <path>             -> path of a radio item to link against
    #       "<Separator>"      -> create a separator
    #       "<Branch>"         -> create an item to hold sub items (optional)
    #       "<LastBranch>"     -> create a right justified branch 

    def get_main_menu(self, window):
        accel_group = gtk.AccelGroup()

        # This function initializes the item factory.
        # Param 1: The type of menu - can be MenuBar, Menu,
        #          or OptionMenu.
        # Param 2: The path of the menu.
        # Param 3: A reference to an AccelGroup. The item factory sets up
        #          the accelerator table while generating menus.
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)

        # This method generates the menu items. Pass to the item factory
        #  the list of menu items
        item_factory.create_items(self.menu_items)

        # Attach the new accelerator group to the window.
        window.add_accel_group(accel_group)

        # need to keep a reference to item_factory to prevent its destruction
        self.item_factory = item_factory
        # Finally, return the actual menu bar created by the item factory.
        return item_factory.get_widget("<main>")

    def __init__(self):
        self.menu_items = (
            ( "/_File",         None,         None, 0, "<Branch>" ),
            ( "/File/_New",     "<control>N", self.print_hello, 0, None ),
            ( "/File/_Open",    "<control>O", self.print_hello, 0, None ),
            ( "/File/_Save",    "<control>S", self.print_hello, 0, None ),
            ( "/File/Save _As", None,         None, 0, None ),
            ( "/File/sep1",     None,         None, 0, "<Separator>" ),
            ( "/File/Quit",     "<control>Q", gtk.main_quit, 0, None ),
            ( "/_Options",      None,         None, 0, "<Branch>" ),
            ( "/Options/Test",  None,         None, 0, None ),
            ( "/_Help",         None,         None, 0, "<LastBranch>" ),
            ( "/_Help/About",   None,         None, 0, None ),
            )
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("Item Factory")
        window.set_size_request(300, 200)

        main_vbox = gtk.VBox(False, 1)
        main_vbox.set_border_width(1)
        window.add(main_vbox)
        main_vbox.show()

        menubar = self.get_main_menu(window)

        main_vbox.pack_start(menubar, False, True, 0)
        menubar.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ItemFactoryExample()
    main()
