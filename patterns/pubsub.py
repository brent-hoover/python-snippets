#!/usr/bin/env python
#
# [SNIPPET_NAME: Publish/Subscribe]
# [SNIPPET_CATEGORIES: Patterns, PyGTK]
# [SNIPPET_DESCRIPTION: A module providing a minimal implementation of the Publish/Subscribe Pattern]
# [SNIPPET_AUTHOR: Bastian Kennel <bastian.kennel@gmail.com>]
# [SNIPPET_LICENSE: GPL]

"""This Pattern is very useful for communication between indepentdent parts of a program."""

# wikipedia: http://en.wikipedia.org/wiki/Publish/subscribe

import gtk
import logging

subscriptions = {}

def subscribe(message, subscriber):
    """
    
    Subscribes the subscriber to a message. Subscriber has to be callable and
    accept all parameters the message issues.
    Message can be anything, but should be a primitive (like a string) to not
    complicate subscriber implementations.
    
    """
    if not message in subscriptions:
        subscriptions[message] = [subscriber]
    else:
        subscriptions[message].append(subscriber)
        
def publish(message, *args, **kwargs):
    """
    
    Publish a message with respective arguments.
    Call every subscriber to this message and pass the arguments.
    
    """
    if not message in subscriptions:
        logging.info("Message with no Subscribers: " + str(message))
        return
    for subscriber in subscriptions[message]:
        try:
            subscriber(*args, **kwargs)
        except Exception, e:
            logging.error("Subscriber " + str(subscriber) + " could not handle message " + str(message) + ": " + str(args) + str(kwargs))
            
def unsubscribe(message, subscriber):
    """Unsubscribe the subscriber from the message."""
    if not message in subscriptions:
        logging.info("No Message to unsibscribe from: " + str(message))
    elif not subscriber in subscriptions[message]:
        logging.info("Subscriber " + str(subscriber) + " not subscribed for message " + str(message))
    else:
        subscriptions[message].remove(subscriber)
        
        
# # # # Example Code from here on # # # #

# example taken from the python-snippet 'Buttons'

import pygtk
pygtk.require('2.0')
import gtk

def xpm_label_box(parent, xpm_filename, label_text):
    # Create box for xpm and label
    box1 = gtk.HBox(False, 0)
    box1.set_border_width(2)

    # Now on to the image stuff
    image = gtk.Image()
    image.set_from_file(xpm_filename)

    # Create a label for the button
    label = gtk.Label(label_text)

    # Pack the pixmap and label into the box
    box1.pack_start(image, False, False, 3)
    box1.pack_start(label, False, False, 3)

    image.show()
    label.show()
    return box1
    

# the message to communicate with    
MESSAGE = "THE_message"

# dumb subscription stub
def someFunctionAnywhereDoingAnything(some, data, optional=42):
    print "I received ", some, data, " along with optional ", optional

class Buttons:
    # Our usual callback method
    def callback(self, widget, data=None):
        print "Hello again - %s was pressed" % data
        # publishing
        publish(MESSAGE, "an", " invitation", optional = "nothing.")

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Image'd Buttons!")

        # It's a good idea to do this for all windows.
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        # Sets the border width of the window.
        self.window.set_border_width(10)

        # Create a new button
        button = gtk.Button()

        # Connect the "clicked" signal of the button to our callback
        button.connect("clicked", self.callback, "cool button")

        # This calls our box creating function
        box1 = xpm_label_box(self.window, "info.xpm", "cool button")

        # Pack and show all our widgets
        button.add(box1)

        box1.show()
        button.show()

        self.window.add(button)
        self.window.show()

def main():
    # subscribing
    subscribe(MESSAGE, someFunctionAnywhereDoingAnything)
    gtk.main()
    return 0     

if __name__ == "__main__":
    Buttons()
    main()
