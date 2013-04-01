#!/usr/bin/env python
#
# [SNIPPET_NAME: Range Widgets]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using Range Widgets]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-RangeWidgetEample.html, http://www.pygtk.org/docs/pygtk/class-gtkrange.html]

# example rangewidgets.py

import pygtk
pygtk.require('2.0')
import gtk

# Convenience functions

def make_menu_item(name, callback, data=None):
    item = gtk.MenuItem(name)
    item.connect("activate", callback, data)
    item.show()
    return item

def scale_set_default_values(scale):
    scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
    scale.set_digits(1)
    scale.set_value_pos(gtk.POS_TOP)
    scale.set_draw_value(True)

class RangeWidgets:
    def cb_pos_menu_select(self, item, pos):
        # Set the value position on both scale widgets
        self.hscale.set_value_pos(pos)
        self.vscale.set_value_pos(pos)

    def cb_update_menu_select(self, item, policy):
        # Set the update policy for both scale widgets
        self.hscale.set_update_policy(policy)
        self.vscale.set_update_policy(policy)

    def cb_digits_scale(self, adj):
        # Set the number of decimal places to which adj->value is rounded
        self.hscale.set_digits(adj.value)
        self.vscale.set_digits(adj.value)

    def cb_page_size(self, get, set):
        # Set the page size and page increment size of the sample
        # adjustment to the value specified by the "Page Size" scale
        set.page_size = get.value
        set.page_incr = get.value
        # Now emit the "changed" signal to reconfigure all the widgets that
        # are attached to this adjustment
        set.emit("changed")

    def cb_draw_value(self, button):
        # Turn the value display on the scale widgets off or on depending
        # on the state of the checkbutton
        self.hscale.set_draw_value(button.get_active())
        self.vscale.set_draw_value(button.get_active())  

    # makes the sample window

    def __init__(self):
        # Standard window-creating stuff
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_title("range controls")

        box1 = gtk.VBox(False, 0)
        self.window.add(box1)
        box1.show()

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        # value, lower, upper, step_increment, page_increment, page_size
        # Note that the page_size value only makes a difference for
        # scrollbar widgets, and the highest value you'll get is actually
        # (upper - page_size).
        adj1 = gtk.Adjustment(0.0, 0.0, 101.0, 0.1, 1.0, 1.0)
  
        self.vscale = gtk.VScale(adj1)
        scale_set_default_values(self.vscale)
        box2.pack_start(self.vscale, True, True, 0)
        self.vscale.show()

        box3 = gtk.VBox(False, 10)
        box2.pack_start(box3, True, True, 0)
        box3.show()

        # Reuse the same adjustment
        self.hscale = gtk.HScale(adj1)
        self.hscale.set_size_request(200, 30)
        scale_set_default_values(self.hscale)
        box3.pack_start(self.hscale, True, True, 0)
        self.hscale.show()

        # Reuse the same adjustment again
        scrollbar = gtk.HScrollbar(adj1)
        # Notice how this causes the scales to always be updated
        # continuously when the scrollbar is moved
        scrollbar.set_update_policy(gtk.UPDATE_CONTINUOUS)
        box3.pack_start(scrollbar, True, True, 0)
        scrollbar.show()

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        # A checkbutton to control whether the value is displayed or not
        button = gtk.CheckButton("Display value on scale widgets")
        button.set_active(True)
        button.connect("toggled", self.cb_draw_value)
        box2.pack_start(button, True, True, 0)
        button.show()
  
        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)

        # An option menu to change the position of the value
        label = gtk.Label("Scale Value Position:")
        box2.pack_start(label, False, False, 0)
        label.show()
  
        opt = gtk.OptionMenu()
        menu = gtk.Menu()

        item = make_menu_item ("Top", self.cb_pos_menu_select, gtk.POS_TOP)
        menu.append(item)
  
        item = make_menu_item ("Bottom", self.cb_pos_menu_select,
                               gtk.POS_BOTTOM)
        menu.append(item)
  
        item = make_menu_item ("Left", self.cb_pos_menu_select, gtk.POS_LEFT)
        menu.append(item)
  
        item = make_menu_item ("Right", self.cb_pos_menu_select, gtk.POS_RIGHT)
        menu.append(item)
  
        opt.set_menu(menu)
        box2.pack_start(opt, True, True, 0)
        opt.show()

        box1.pack_start(box2, True, True, 0)
        box2.show()

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)

        # Yet another option menu, this time for the update policy of the
        # scale widgets
        label = gtk.Label("Scale Update Policy:")
        box2.pack_start(label, False, False, 0)
        label.show()
  
        opt = gtk.OptionMenu()
        menu = gtk.Menu()
  
        item = make_menu_item("Continuous", self.cb_update_menu_select,
                              gtk.UPDATE_CONTINUOUS)
        menu.append(item)
  
        item = make_menu_item ("Discontinuous", self.cb_update_menu_select,
                               gtk.UPDATE_DISCONTINUOUS)
        menu.append(item)
  
        item = make_menu_item ("Delayed", self.cb_update_menu_select,
                               gtk.UPDATE_DELAYED)
        menu.append(item)
  
        opt.set_menu(menu)
        box2.pack_start(opt, True, True, 0)
        opt.show()
  
        box1.pack_start(box2, True, True, 0)
        box2.show()

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
  
        # An HScale widget for adjusting the number of digits on the
        # sample scales.
        label = gtk.Label("Scale Digits:")
        box2.pack_start(label, False, False, 0)
        label.show()

        adj2 = gtk.Adjustment(1.0, 0.0, 5.0, 1.0, 1.0, 0.0)
        adj2.connect("value_changed", self.cb_digits_scale)
        scale = gtk.HScale(adj2)
        scale.set_digits(0)
        box2.pack_start(scale, True, True, 0)
        scale.show()

        box1.pack_start(box2, True, True, 0)
        box2.show()
  
        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
  
        # And, one last HScale widget for adjusting the page size of the
        # scrollbar.
        label = gtk.Label("Scrollbar Page Size:")
        box2.pack_start(label, False, False, 0)
        label.show()

        adj2 = gtk.Adjustment(1.0, 1.0, 101.0, 1.0, 1.0, 0.0)
        adj2.connect("value_changed", self.cb_page_size, adj1)
        scale = gtk.HScale(adj2)
        scale.set_digits(0)
        box2.pack_start(scale, True, True, 0)
        scale.show()

        box1.pack_start(box2, True, True, 0)
        box2.show()

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button = gtk.Button("Quit")
        button.connect("clicked", lambda w: gtk.main_quit())
        box2.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        self.window.show()

def main():
    gtk.main()
    return 0            

if __name__ == "__main__":
    RangeWidgets()
    main()
