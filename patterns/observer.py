#!/usr/bin/env python
#
# [SNIPPET_NAME: Observer]
# [SNIPPET_CATEGORIES: Patterns]
# [SNIPPET_DESCRIPTION: A module providing a basic implementation of the Observer pattern]
# [SNIPPET_AUTHOR: Scott Ferguson <scottwferg@gmail.com>]
# [SNIPPET_LICENSE: GPL]

"""This pattern is great for allowing asynchronous modules of your application to communicate
when something happens.  This is very useful in threaded GUI applications when you want a
threaded operation to alert the main UI that an operation has been performed and you have a
tangible result."""

# wikipedia: http://en.wikipedia.org/wiki/Observer_pattern

class Observer:
    """An observer simply watches a concrete subject, waiting for something to occur.
    The update() function will always be defined in the observer."""
    def update(self):
        return;

class Subject:
    """The subject is watched by one or many observers.  When something occurs within the
    subject, all observers are notified."""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Add a new observer to self"""
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove an observer from self"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args):
        """Notify all observers that something occurred"""
        for observer in self._observers:
            observer.update(*args)

# # # # Example Code from here on # # # #

"""In this sample code the application class creates a widget, and then fires off
an event on that widget.  It is always watching the widget, waiting for something
to occur."""

import time

class widget(Subject):
    _counter = 1

    def __init__(self, client):
        Subject.__init__(self)
        self.attach(client)
    
    def _respond(self):
        self.notify(self._counter)
        self._counter = self._counter + 1

    def wait_for_response(self):
        self._respond()
        time.sleep(2)
        self._respond()
        time.sleep(2)
        self._respond()
        time.sleep(2)
        self._respond()

class application(Observer):
    def __init__(self):
        self.button = widget(self)

    def click_widget(self):
        self.button.wait_for_response()
    
    def update(self, *args):
        print 'Updated! The subject said: %s' % args[0]

if __name__ == '__main__':
    app = application()
    app.click_widget()
