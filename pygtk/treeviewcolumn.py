#!/usr/bin/env python
#
# [SNIPPET_NAME: Tree View Column]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using tree view columns]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-TreeViewWidget.html, http://www.pygtk.org/docs/pygtk/class-gtktreeviewcolumn.html]

# example treeviewcolumn.py

import pygtk
pygtk.require('2.0')
import gtk

class TreeViewColumnExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def make_pb(self, tvcolumn, cell, model, iter):
        stock = model.get_value(iter, 1)
        pb = self.treeview.render_icon(stock, gtk.ICON_SIZE_MENU, None)
        cell.set_property('pixbuf', pb)
        return

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("TreeViewColumn Example")

        #self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(str, str, str, 'gboolean')

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Pixbuf and Text')
        self.tvcolumn1 = gtk.TreeViewColumn('Text Only')

        # add a row with text and a stock item - color strings for
        # the background
        self.liststore.append(['Open', gtk.STOCK_OPEN, 'Open a File', True])
        self.liststore.append(['New', gtk.STOCK_NEW, 'New File', True])
        self.liststore.append(['Print', gtk.STOCK_PRINT, 'Print File', False])

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        # create a CellRenderers to render the data
        self.cellpb = gtk.CellRendererPixbuf()
        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        # set background color property
        self.cellpb.set_property('cell-background', 'yellow')
        self.cell.set_property('cell-background', 'cyan')
        self.cell1.set_property('cell-background', 'pink')


        # add the cells to the columns - 2 in the first
        self.tvcolumn.pack_start(self.cellpb, False)
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        # set the cell attributes to the appropriate liststore column
        # GTK+ 2.0 doesn't support the "stock_id" property
        if gtk.gtk_version[1] < 2:
            self.tvcolumn.set_cell_data_func(self.cellpb, self.make_pb)
        else:
            self.tvcolumn.set_attributes(self.cellpb, stock_id=1)
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=2,
                                      cell_background_set=3)

        # make treeview searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = TreeViewColumnExample()
    main()
