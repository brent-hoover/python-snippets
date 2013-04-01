#!/usr/bin/env python
#
# [SNIPPET_NAME: Fixed]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Creating a fixed container]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Fixed.html, http://www.pygtk.org/docs/pygtk/class-gtkfixed.html]

# example fixed.py

import pygtk
pygtk.require('2.0')
import gtk

class FixedExample:
    # This callback method moves the button to a new position
    # in the Fixed container.
    def move_button(self, widget):
        self.x = (self.x+30)%300
        self.y = (self.y+50)%300
        self.fixed.move(widget, self.x, self.y) 

    def __init__(self):
        self.x = 50
        self.y = 50

        # Create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Fixed Container")

        # Here we connect the "destroy" event to a signal handler 
        window.connect("destroy", lambda w: gtk.main_quit())
 
        # Sets the border width of the window.
        window.set_border_width(10)

        # Create a Fixed Container
        self.fixed = gtk.Fixed()
        window.add(self.fixed)
        self.fixed.show()
  
        for i in range(1, 4):
            # Creates a new button with the label "Press me"
            button = gtk.Button("Press me")
  
            # When the button receives the "clicked" signal, it will call the
            # method move_button().
            button.connect("clicked", self.move_button)
  
            # This packs the button into the fixed containers window.
            self.fixed.put(button, i*50, i*50)
  
            # The final step is to display this newly created widget.
            button.show()

        # Display the window
        window.show()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    FixedExample()
    main()
