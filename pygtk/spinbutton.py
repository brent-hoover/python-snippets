#!/usr/bin/env python
#
# [SNIPPET_NAME: Spin Button]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Adding a spin button]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-SpinButtons.html, http://www.pygtk.org/docs/pygtk/class-gtkspinbutton.html]

# example spinbutton.py

import pygtk
pygtk.require('2.0')
import gtk

class SpinButtonExample:
    def toggle_snap(self, widget, spin):
        spin.set_snap_to_ticks(widget.get_active())

    def toggle_numeric(self, widget, spin):
        spin.set_numeric(widget.get_active())

    def change_digits(self, widget, spin, spin1):
        spin1.set_digits(spin.get_value_as_int())

    def get_value(self, widget, data, spin, spin2, label):
        if data == 1:
            buf = "%d" % spin.get_value_as_int()
        else:
            buf = "%0.*f" % (spin2.get_value_as_int(),
                             spin.get_value())
        label.set_text(buf)

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("Spin Button")

        main_vbox = gtk.VBox(False, 5)
        main_vbox.set_border_width(10)
        window.add(main_vbox)

        frame = gtk.Frame("Not accelerated")
        main_vbox.pack_start(frame, True, True, 0)
  
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)

        # Day, month, year spinners
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, True, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        label = gtk.Label("Day :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(1.0, 1.0, 31.0, 1.0, 5.0, 0.0)
        spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_wrap(True)
        vbox2.pack_start(spinner, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Month :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        adj = gtk.Adjustment(1.0, 1.0, 12.0, 1.0, 5.0, 0.0)
        spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_wrap(True)
        vbox2.pack_start(spinner, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Year :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(1998.0, 0.0, 2100.0, 1.0, 100.0, 0.0)
        spinner = gtk.SpinButton(adj, 0, 0)
        spinner.set_wrap(False)
        spinner.set_size_request(55, -1)
        vbox2.pack_start(spinner, False, True, 0)
  
        frame = gtk.Frame("Accelerated")
        main_vbox.pack_start(frame, True, True, 0)
  
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Value :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.5, 100.0, 0.0)
        spinner1 = gtk.SpinButton(adj, 1.0, 2)
        spinner1.set_wrap(True)
        spinner1.set_size_request(100, -1)
        vbox2.pack_start(spinner1, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Digits :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(2, 1, 5, 1, 1, 0)
        spinner2 = gtk.SpinButton(adj, 0.0, 0)
        spinner2.set_wrap(True)
        adj.connect("value_changed", self.change_digits, spinner2, spinner1)
        vbox2.pack_start(spinner2, False, True, 0)
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)

        button = gtk.CheckButton("Snap to 0.5-ticks")
        button.connect("clicked", self.toggle_snap, spinner1)
        vbox.pack_start(button, True, True, 0)
        button.set_active(True)
  
        button = gtk.CheckButton("Numeric only input mode")
        button.connect("clicked", self.toggle_numeric, spinner1)
        vbox.pack_start(button, True, True, 0)
        button.set_active(True)
  
        val_label = gtk.Label("")
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
        button = gtk.Button("Value as Int")
        button.connect("clicked", self.get_value, 1, spinner1, spinner2,
                       val_label)
        hbox.pack_start(button, True, True, 5)
  
        button = gtk.Button("Value as Float")
        button.connect("clicked", self.get_value, 2, spinner1, spinner2,
                       val_label)
        hbox.pack_start(button, True, True, 5)
  
        vbox.pack_start(val_label, True, True, 0)
        val_label.set_text("0")
  
        hbox = gtk.HBox(False, 0)
        main_vbox.pack_start(hbox, False, True, 0)
  
        button = gtk.Button("Close")
        button.connect("clicked", lambda w: gtk.main_quit())
        hbox.pack_start(button, True, True, 5)
        window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    SpinButtonExample()
    main()
