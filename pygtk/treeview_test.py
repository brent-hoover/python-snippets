#!/usr/bin/env python
#
# [SNIPPET_NAME: Treeview Test]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: A test treeview application]

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

    def str_obj(self, tvcolumn, cell, model, iter):
        obj = model.get_value(iter, 0)
        cell.set_property('text', str(obj))
        return

    def toggled(self, cell, path):
        iter = self.treestore.get_iter(path)
        value = not self.treestore.get_value(iter, 1)
        self.treestore.set_value(iter, 1, value)
        return

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Example")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        self.scrolledwindow = gtk.ScrolledWindow()
        self.vbox = gtk.VBox()
        self.hbox = gtk.HBox()
        self.vbox.pack_start(self.scrolledwindow, True)
        self.vbox.pack_start(self.hbox, False)
        self.b0 = gtk.Button('Expand All')
        self.b1 = gtk.Button('Collapse All')
        self.hbox.pack_start(self.b0)
        self.hbox.pack_start(self.b1)

        # create a treestore with one string column to use as the model
        self.treestore = gtk.TreeStore(str, str)

        # create the TreeView using treestore
        self.treeview = gtk.TreeView(self.treestore)

       # create a CellRenderer to render the data
        self.cell = gtk.CellRendererText()

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Part No.', self.cell)
        self.tvcolumn1 = gtk.TreeViewColumn('Part Name', self.cell)

        self.tvcolumn.add_attribute(self.cell, 'text', 0)
        self.tvcolumn1.add_attribute(self.cell, 'text', 1)

        # add data
        iter = self.treestore.append(None, ['123', 'Widget'])
        self.treestore.append(iter, ['123-1', 'Widget Frammer'])
        self.treestore.append(iter, ['123-2', 'Widget Whatsit'])
        self.treestore.append(iter, ['123-3', 'Widget Thingy'])
        iter = self.treestore.append(None, ['456', 'Thingamabob'])
        self.treestore.append(iter, ['456-1', 'Thingamabob Frammer'])
        iter1 = self.treestore.append(iter, ['456-2', 'Thingamabob Bunger'])
        self.treestore.append(iter1, ['456-2-1', 'Thingamabob Bunger Spring'])

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        self.treeview.set_expander_column(self.tvcolumn1)

        self.b0.connect_object('clicked', gtk.TreeView.expand_all,
                               self.treeview)
        self.b1.connect_object('clicked', gtk.TreeView.collapse_all,
                              self.treeview)
        # make treeview searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        #self.treeview.set_reorderable(True)

        self.treeview.enable_model_drag_source(0, [("STRING", 0, 0),
                                                   ('text/plain', 0, 0)
                                                   ],
                                               gtk.gdk.ACTION_DEFAULT)
        self.treeview.enable_model_drag_dest([("STRING", 0, 0),
                                              ('text/plain', 0, 0),
                                              ('text/uri-list', 0, 0)
                                              ],
                                             gtk.gdk.ACTION_DEFAULT)

        self.treeview.connect("drag_data_get", self.drag_data_get_data)
        self.treeview.connect("drag_data_received",
                              self.drag_data_received_data)

        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)

        self.window.show_all()

    def drag_data_get_data(self, treeview, context, selection, target, etime):
        treeselection = treeview.get_selection()
        model, iter = treeselection.get_selected()
        data = model.get_value(iter, 1)
        print data
        selection.set('text/plain', 8, data)

    def drag_data_received_data(self, treeview, context, x, y, selection,
                                info, etime):
        print selection.target, selection.type, selection.format, selection.data
        drop_info = treeview.get_dest_row_at_pos(x, y)
        if drop_info:
            model = treeview.get_model()
            path, position = drop_info
            data = selection.data
            print path, data, model.get_value(model.get_iter(path), 1)
        return

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = TreeViewColumnExample()
    main()
