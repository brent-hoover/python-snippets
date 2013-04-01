#!/usr/bin/env python
#
# [SNIPPET_NAME: Center window]
# [SNIPPET_CATEGORIES: PyQt4]
# [SNIPPET_DESCRIPTION: A example of how to centre a window]
# [SNIPPET_AUTHOR: Darren Worrall <dw@darrenworrall.co.uk>]
# [SNIPPET_LICENSE: GPL]

# example centrewindow.py

import sys
from PyQt4 import QtGui, QtCore

class CentreWindow(QtGui.QWidget):
    """
    An example of how to centre a window
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Centre window')
        # Set the window dimensions
        self.resize(200,50)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        
        # Create a push button labelled 'Centre' and add it to our layout
        btn = QtGui.QPushButton('Centre', self)
        self.vbox.addWidget(btn)
        
        # Connect the clicked signal to the centre handler
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.centre)

    def centre(self):
        """
        Center the window on screen. This implemention will handle the window
        being resized or the screen resolution changing.
        """
        # Get the current screens' dimensions...
        screen = QtGui.QDesktopWidget().screenGeometry()
        # ... and get this windows' dimensions
        mysize = self.geometry()
        # The horizontal position is calulated as screenwidth - windowwidth /2
        hpos = ( screen.width() - mysize.width() ) / 2
        # And vertical position the same, but with the height dimensions
        vpos = ( screen.height() - mysize.height() ) / 2
        # And the move call repositions the window
        self.move(hpos, vpos)


# If the program is run directly or passed as an argument to the python
# interpreter then create a CentreWindow instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = CentreWindow()
    gui.show()
    app.exec_()
