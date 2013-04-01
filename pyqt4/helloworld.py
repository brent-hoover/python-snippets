#!/usr/bin/env python
#
# [SNIPPET_NAME: Hello World]
# [SNIPPET_CATEGORIES: PyQt4]
# [SNIPPET_DESCRIPTION: A simple hello world program]
# [SNIPPET_AUTHOR: Darren Worrall <dw@darrenworrall.co.uk>]
# [SNIPPET_LICENSE: GPL]

# example helloworld.py

import sys
from PyQt4 import QtGui, QtCore

class HelloWorld(QtGui.QWidget):
    """
    An example hello world application
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Hello world!')
        # Set the window dimensions
        self.resize(200,50)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        
        # Create a push button labelled 'Hello world' and add it to our layout
        btn = QtGui.QPushButton('Hello world!', self)
        self.vbox.addWidget(btn)
        
        # Connect the clicked signal to the hello handler
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.hello)

    def hello(self):
        """
        Handler called when hello world is clicked
        """
        print 'Hello world!'


# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = HelloWorld()
    gui.show()
    app.exec_()
