#!/usr/bin/env python
#
# [SNIPPET_NAME: Tree Model Filter]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: A tree model filter example]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-TreeModelSortAndTreeModelFilter.html, http://www.pygtk.org/docs/pygtk/class-gtktreemodelfilter.html]

# example treemodelfilter.py

import pygtk
pygtk.require('2.0')
import gtk

bugdata="""120595 NEW Custom GtkTreeModelFilter wrappers need
121339 RESO dsextras.py installation directory is incorrect
121611 RESO argument is guint, should be guint32
121943 RESO gtk.mainiteration and gtk.mainloop defeat the caller's ex...
122260 RESO Could not compile
122569 NEW gtk.Window derived class segfaults
122591 RESO cannot return None from CellRenderer.on_start_editing
122755 RESO _wrap_gdk_window_new needs to ref return value
122786 RESO don't import Numeric until it is first used
123014 NEW PyGtk build problem on Win32 using the 'distutils' approach.
123037 NEW gtk.ListStore.set_column_types is missing
123456 RESO ItemFactory.create_items and <ImageItem> bug
123458 NEED pygtk does not wrap all of gdk-pixbuf
123891 NEW gobject.PARAM_CONSTRUCT problem
124181 NEED Python Shell inside a gtk GUI
124338 RESO Memleak when using pixbuf
124593 RESO TreeModel.iter_children should accept None as parent
125172 RESO gtk.TreeModelSort returns an unusable object
125272 RESO error in gtk_widget_translate_coordinates wrapping
125445 NEW pygtk gives no acces to PangoLayoutIter's
125533 RESO set_skip_taskbar_hint and set_skip_pager_hint not wrapped
126109 RESO gtk.Entry focus_out event core
126323 RESO gtk_disable_setlocale cannot be used
126406 RESO gtk.TreeView.expand_row() should return gboolean not None
126479 RESO None iter's in custom TreeModel cause SystemException's
127083 RESO Binding generation of methods which use gpointer does not...
127178 RESO gtk.Widget color modify methods do not allow None for col...
127504 NEW wrap GtkTreeViewColumnDropFunc
128623 RESO Allow NULL as set_tip argument
128988 RESO missing space in prototype confuses h2def.py
129032 NEW GObject Interfaces (GInterface) support
129414 RESO h2def.py doesn't see gda_log_enable()
129490 RESO Provide hardware_keycode to python
129754 RESO memory leak with gtk.gdk.pixmap_foreign_new()
129843 NEW Make all constructors work through g_object_new()
129966 RESO convert GValue containing GValueArray to PyObject
131837 RESO Cannot set or get \"markup\" property from CellRendererText
132040 NEW abusing setdefaultencoding()
132058 RESO gtkgl bus error on constructor to gtk.gl.Area
132507 RESO gtk_accel_group_connect seems to be missing
132837 NEW set_from_pixmap creates a different gtk.Image than set_fr...
133681 RESO memory leak in gdk.drawable.get_image
134462 RESO pygtk2 segfaults
134491 RESO OverflowError occurs when menu pops up.
134494 RESO The Definition of argument for gtk.gdk.Pixbuf.fill should...
135279 RESO codegen is using private functions
135439 RESO Integrate SDL into pygtk widgets
135963 RESO gc of gtk.ListStore aborts intrepeter after gtk.threads_i...
136204 RESO GtkTextSearchFlags warning
136205 RESO GdkPixbuf.fill passed arg changed type originating crash
136297 RESO Explanatory additions to gtk.DrawingArea
136597 RESO gtkgl still referenced in build files
136688 RESO installation directory of pygtk 2.2
136705 RESO mainquit vs. main_quit usage
136707 RESO gtk.gdk.Window.raise uses reserved keyword.
136731 RESO setup.py should not install the libglade DLL
136811 RESO h2def ignores some functions
136984 RESO Seemingly Invalid Flag for gtk.MessageDialog
136989 NEW should pixbufloader throw two GErrors?
137086 NEW gtk.gdk.window_lookup assertion
137091 RESO \"constants\" for selection atoms
137935 RESO description of gtk.gdk.atom_intern() should be in gtk.gdk...
137969 NEW GenericTreeModel/TreeSelection returning GtkTreeIter inst...
138104 RESO gtk_widget_style_get_property is not wrapped
138163 VERI NOTA gtk.main_iteration(TRUE) unblocks every .1 seconds
138476 RESO gtk.Layout is needed by gnome.canvas but is missing from ...
138487 RESO PyGTK Tutorial: in Calendar sample date string is 1 day b...
138576 RESO gtk.IconSet now has 2 constructors in gtk.defs, while on...
138619 UNCO codegen/definitions.py could use some refactoring
138772 RESO Callback parameters to input_add are incorrect
138804 UNCO In gtk2.4, gdk_font_get_display and gdk_pixmap_lookup is ...
138944 UNCO Cannot import gtk when pygtk installed using 'make install'
139128 UNCO All constructors should be defined as constructors
139130 NEW GtkEntry's constructor needs to be rewritten
139312 NEED gtk.gdk.Window.get_screen method undocumented.
139921 RESO Support tp_new
140071 NEW Register custom widget classes.
140665 RESO TypeError when creating user defined signals having third...
140718 UNCO Enhance codegen with user defined type wrapper.
140946 UNCO filechooser example broken
141042 RESO Garbage collection causes lossage in Pango
141886 UNCO Add a PyGEnum_Type
142030 RESO Possible ref count error in gtk.GC
142738 RESO Fatal error with multi-depth menus
142997 UNCO require() breaks sys.path if libs found in /usr/local/r/local"""

class TreeModelFilterExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("TreeModelFilter Example")

        self.window.set_size_request(400, 400)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(int, str, str)

        self.modelfilter = self.liststore.filter_new()

        # create the TreeView
        self.treeview = gtk.TreeView()

        # create the TreeViewColumns to display the data
        self.treeview.columns = [None]*3
        self.treeview.columns[0] = gtk.TreeViewColumn('Bug No.')
        self.treeview.columns[1] = gtk.TreeViewColumn('Status')
        self.treeview.columns[2] = gtk.TreeViewColumn('Description')

        # add bug data
        self.states = []
        for line in bugdata.split('\n'):
            l = line.split()
            self.liststore.append([int(l[0]), l[1], ' '.join(l[2:])])
            if not l[1] in self.states:
                self.states.append(l[1])

        self.show_states = self.states[:]
        self.modelfilter.set_visible_func(self.visible_cb, self.show_states)

        self.treeview.set_model(self.modelfilter)

        for n in range(3):
            # add columns to treeview
            self.treeview.append_column(self.treeview.columns[n])
            # create a CellRenderers to render the data
            self.treeview.columns[n].cell = gtk.CellRendererText()
            # add the cells to the columns
            self.treeview.columns[n].pack_start(self.treeview.columns[n].cell,
                                                True)
            # set the cell attributes to the appropriate liststore column
            self.treeview.columns[n].set_attributes(
                self.treeview.columns[n].cell, text=n)


        # make treeview searchable
        self.treeview.set_search_column(3)

        # make ui layout
        self.vbox = gtk.VBox()
        self.scrolledwindow = gtk.ScrolledWindow()
        self.bbox = gtk.HButtonBox()
        self.vbox.pack_start(self.scrolledwindow)
        self.vbox.pack_start(self.bbox, False)
        # create toggle buttons to select filtering based on
        # bug state and set buttons active
        for state in self.states:
            b = gtk.ToggleButton(state)
            self.bbox.pack_start(b)
            b.set_active(True)
            b.connect('toggled', self.check_buttons)

        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)

        self.window.show_all()
        return

    # visibility determined by state matching active toggle buttons
    def visible_cb(self, model, iter, data):
        return model.get_value(iter, 1) in data

    # build list of bug states to show and then refilter
    def check_buttons(self, tb):
        del self.show_states[:]
        for b in self.bbox.get_children():
            if b.get_active():
                self.show_states.append(b.get_label())
        self.modelfilter.refilter()
        return

def main():
    gtk.main()

if __name__ == "__main__":
    tmfexample = TreeModelFilterExample()
    main()
