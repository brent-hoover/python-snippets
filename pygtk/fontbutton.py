#!/usr/bin/env python
#
# [SNIPPET_NAME: Font Button]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a font button]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkfontbutton.html]

import pygtk
pygtk.require('2.0')
import gtk

class FontButtonExample:
    def __init__(self):
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox()
        window.add(vbox)
        hbox = gtk.HBox()
        vbox.pack_start(hbox, False)
        label = gtk.Label('Current Font:')
        hbox.pack_start(label, False)
        fontbutton = gtk.FontButton('Monospace Italic 14')
        fontbutton.set_use_font(True)
        fontbutton.set_title('Select a font')
        fontbutton.connect('font-set', self.font_set_cb)
        hbox.pack_start(fontbutton)
        self.fontbutton = fontbutton
        bbox = gtk.HButtonBox()
        vbox.pack_start(bbox, False)
        b = gtk.ToggleButton('use_font', False)
        b.connect('toggled', self.use_font_cb)
        b.set_active(True)
        bbox.pack_start(b)
        b = gtk.ToggleButton('use_size', False)
        b.connect('toggled', self.use_size_cb)
        b.set_active(False)
        bbox.pack_start(b)
        b = gtk.ToggleButton('show_style', False)
        b.connect('toggled', self.show_style_cb)
        b.set_active(True)
        bbox.pack_start(b)
        b = gtk.ToggleButton('show_size', False)
        b.connect('toggled', self.show_size_cb)
        b.set_active(True)
        bbox.pack_start(b)
        window.show_all()
        return
    def use_font_cb(self, togglebutton):
        self.fontbutton.set_use_font(togglebutton.get_active())
        return
    def use_size_cb(self, togglebutton):
        self.fontbutton.set_use_size(togglebutton.get_active())
        return
    def show_style_cb(self, togglebutton):
        self.fontbutton.set_show_style(togglebutton.get_active())
        return
    def show_size_cb(self, togglebutton):
        self.fontbutton.set_show_size(togglebutton.get_active())
        return
    def font_set_cb(self, fontbutton):
        font = fontbutton.get_font_name()
        print 'You have selected the font:', font
        return

def main():
    gtk.main()


if __name__ == '__main__':
    cbe = FontButtonExample()
    main()
