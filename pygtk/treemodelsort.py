#!/usr/bin/env python
#
# [SNIPPET_NAME: Tree Model Sort]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Sorting a tree model]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-TreeModelSortAndTreeModelFilter.html]

# example treemodelsort.py

import pygtk
pygtk.require('2.0')
import gtk
import random

class TreeModelSortExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def add_row(self, b):
        rand = self.rand
        # add a row of random ints
        i0 = self.w[0].sm.get_model().append([rand.randint(0, 1000),
                                              rand.randint(0, 1000000),
                                              rand.randint(-10000, 10000)])
        # select the new row in each view
        for n in range(3):
            sel = self.w[n].tv.get_selection()
            i1 = self.w[n].sm.convert_child_iter_to_iter(None, i0)
            sel.select_iter(i1)

    def __init__(self):
        # create a liststore with three int columns
        self.liststore = gtk.ListStore(int, int, int)

        # create a random number generator
        self.rand = random.Random()

        # Create new windows
        self.w = [None] * 3
        
        for n in range(3):
            self.w[n] = gtk.Window(gtk.WINDOW_TOPLEVEL)
            win = self.w[n]
            win.set_title("TreeModelSort Example %i" % n)
            win.set_size_request(220, 200)
            win.connect("delete_event", self.delete_event)
            win.vbox = gtk.VBox()
            win.add(win.vbox)
            win.sw = gtk.ScrolledWindow()
            win.sm = gtk.TreeModelSort(self.liststore)
            # Set sort column
            win.sm.set_sort_column_id(n, gtk.SORT_ASCENDING)
            win.tv = gtk.TreeView(win.sm)
            win.vbox.pack_start(win.sw)
            win.b = gtk.Button('Add a Row')
            win.b.connect('clicked', self.add_row)
            win.vbox.pack_start(win.b, False)
            win.sw.add(win.tv)
            win.tv.column = [None]*3
            win.tv.column[0] = gtk.TreeViewColumn('0-1000')
            win.tv.column[1] = gtk.TreeViewColumn('0-1000000')
            win.tv.column[2] = gtk.TreeViewColumn('-10000-10000')
            win.tv.cell = [None]*3
            for i in range(3):
                win.tv.cell[i] = gtk.CellRendererText()
                win.tv.append_column(win.tv.column[i])
                win.tv.column[i].set_sort_column_id(i)
                win.tv.column[i].pack_start(win.tv.cell[i], True)
                win.tv.column[i].set_attributes(win.tv.cell[i], text=i)
            win.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tmsexample = TreeModelSortExample()
    main()
