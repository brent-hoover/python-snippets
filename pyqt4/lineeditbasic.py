#!/usr/bin/env python
#
# [SNIPPET_NAME: Line Edit Basic]
# [SNIPPET_CATEGORIES: PyQt4]
# [SNIPPET_DESCRIPTION: An basic example of a line edit widget]
# [SNIPPET_AUTHOR: Darren Worrall <dw@darrenworrall.co.uk>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qlineedit.html]

# example lineeditbasic.py

import sys
from PyQt4 import QtGui, QtCore

class LineEditBasic(QtGui.QWidget):
    """
    An basic example line edit application
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Line Edit Basic')
        # Set the window dimensions
        self.resize(300,75)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a line edit widget and add it to our layout
        self.le = QtGui.QLineEdit()
        self.vbox.addWidget(self.le)

        # A label to display the text entered
        self.lbl = QtGui.QLabel()
        self.vbox.addWidget(self.lbl)

        # Connect the textChanged signal on the combo box to our handler.
        self.connect(self.le, QtCore.SIGNAL('textChanged(QString)'),
                     self.text_changed)

    def text_changed(self, text):
        """
        Handler called when the text in the entry widget has changed
        """
        self.lbl.setText(text)


# If the program is run directly or passed as an argument to the python
# interpreter then create a LineEditBasic instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = LineEditBasic()
    gui.show()
    app.exec_()
