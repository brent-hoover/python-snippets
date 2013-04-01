#!/usr/bin/env python
#
# [SNIPPET_NAME: Label]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using a label]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtklabel.html]

# example label.py

import pygtk
pygtk.require('2.0')
import gtk

class Labels:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", lambda w: gtk.main_quit())

        self.window.set_title("Label")
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(False, 5)
        self.window.add(hbox)
        hbox.pack_start(vbox, False, False, 0)
        self.window.set_border_width(5)

        frame = gtk.Frame("Normal Label")
        label = gtk.Label("This is a Normal label")
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
  
        frame = gtk.Frame("Multi-line Label")
        label = gtk.Label("This is a Multi-line label.\nSecond line\n"
                             "Third line")
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
  
        frame = gtk.Frame("Left Justified Label")
        label = gtk.Label("This is a Left-Justified\n"
                             "Multi-line label.\nThird      line")
        label.set_justify(gtk.JUSTIFY_LEFT)
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
  
        frame = gtk.Frame("Right Justified Label")
        label = gtk.Label("This is a Right-Justified\nMulti-line label.\n"
                             "Fourth line, (j/k)")
        label.set_justify(gtk.JUSTIFY_RIGHT)
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)

        vbox = gtk.VBox(False, 5)
        hbox.pack_start(vbox, False, False, 0)
        frame = gtk.Frame("Line wrapped label")
        label = gtk.Label("This is an example of a line-wrapped label.  It "
                             "should not be taking up the entire             "
                             "width allocated to it, but automatically "
                             "wraps the words to fit.  "
                             "The time has come, for all good men, to come to "
                             "the aid of their party.  "
                             "The sixth sheik's six sheep's sick.\n"
                             "     It supports multiple paragraphs correctly, "
                             "and  correctly   adds "
                             "many          extra  spaces. ")
        label.set_line_wrap(True)
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
  
        frame = gtk.Frame("Filled, wrapped label")
        label = gtk.Label("This is an example of a line-wrapped, filled label.  "
                             "It should be taking "
                             "up the entire              width allocated to it.  "
                             "Here is a sentence to prove "
                             "my point.  Here is another sentence. "
                             "Here comes the sun, do de do de do.\n"
                             "    This is a new paragraph.\n"
                             "    This is another newer, longer, better "
                             "paragraph.  It is coming to an end, "
                             "unfortunately.")
        label.set_justify(gtk.JUSTIFY_FILL)
        label.set_line_wrap(True)
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
  
        frame = gtk.Frame("Underlined label")
        label = gtk.Label("This label is underlined!\n"
                             "This one is underlined in quite a funky fashion")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_pattern(
            "_________________________ _ _________ _ ______     __ _______ ___")
        frame.add(label)
        vbox.pack_start(frame, False, False, 0)
        self.window.show_all ()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Labels()
    main()
