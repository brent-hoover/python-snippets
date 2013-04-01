#!/usr/bin/env python
#
# [SNIPPET_NAME: Generic Tree Model]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a generic tree model]

import pygtk
pygtk.require('2.0')
import gtk

class MyTreeModel(gtk.GenericTreeModel):
    _column_types = [str, str, int]
    _model_data = [('row %i'%n, 'string %i'%n, n) for n in range(10)]

    def on_get_flags(self):
        return gtk.TREE_MODEL_LIST_ONLY | gtk.TREE_MODEL_ITERS_PERSIST

    def on_get_n_columns(self):
        return len(self._column_types)

    def on_get_column_type(self, index):
        return self._column_types[index]

    def on_get_iter(self, path):
        return self._model_data[path[0]]

    def on_get_path(self, rowref):
        n = 0
        for r in self._model_data:
            if id(r) == id(rowref):
                return n
            n += 1
        raise ValueError, 'Invalid iter'

    def on_get_value(self, rowref, column):
        return rowref[column]

    def on_iter_next(self, rowref):
        n = self.on_get_path(rowref)
        try:
            rowref = self._model_data[n+1]
        except IndexError, msg:
            rowref = None
        return rowref

    def on_iter_children(self, rowref):
        if rowref:
            return None
        if self._model_data:
            return self.on_get_iter((0,))
        return None

    def on_iter_has_child(self, rowref):
        if rowref:
            return False
        if len(self._model_data) > 0:
            return True
        return False

    def on_iter_n_children(self, rowref):
        if rowref:
            return 0
        return len(self._model_data)

    def on_iter_nth_child(self, parent, n):
        if parent:
            return None
        if n < 0 or n >= len(self._model_data):
            return None
        return self._model_data[n]

    def on_iter_parent(self, rowref):
        return None

class GenericTreeModelExample:
    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Generic TreeModel Example")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        self.listmodel = MyTreeModel()

        # create the TreeView
        self.treeview = gtk.TreeView(self.listmodel)

        # create the TreeViewColumn to display the data
        self.tvcolumn0 = gtk.TreeViewColumn('Column 0')
        self.tvcolumn1 = gtk.TreeViewColumn('Column 1')

        # add tvcolumns to treeview
        self.treeview.append_column(self.tvcolumn0)
        self.treeview.append_column(self.tvcolumn1)

        # create a CellRendererText to render the data
        self.cell0 = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        # add the cells to the tvcolumns
        self.tvcolumn0.pack_start(self.cell0, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        self.tvcolumn0.add_attribute(self.cell0, 'text', 0)
        self.tvcolumn1.add_attribute(self.cell1, 'text', 1)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    gtmexample = GenericTreeModelExample()
    main()
