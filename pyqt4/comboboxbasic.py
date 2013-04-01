#!/usr/bin/env python
#
# [SNIPPET_NAME: Combo Box Basic]
# [SNIPPET_CATEGORIES: PyQt4]
# [SNIPPET_DESCRIPTION: An basic example of a combo box]
# [SNIPPET_AUTHOR: Darren Worrall <dw@darrenworrall.co.uk>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qcombobox.html]

# example comboboxbasic.py

import sys
from PyQt4 import QtGui, QtCore

class ComboBoxBasic(QtGui.QWidget):
    """
    An basic example combo box application
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Combo Box Basic')
        # Set the window dimensions
        self.resize(250,50)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a combo box and add it to our layout
        self.combo = QtGui.QComboBox()
        self.vbox.addWidget(self.combo)

        # A label to display our selection
        self.lbl = QtGui.QLabel('Ubuntu')
        # Center align text
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.lbl)

        # You can add items individually:
        self.combo.addItem('Ubuntu')
        self.combo.addItem('Fedora')

        # Or add a sequence in one call
        distrolist = ['Linux Mint', 'Gentoo', 'Mandriva']
        self.combo.addItems(distrolist)
        
        # Connect the activated signal on the combo box to our handler.
        # This is an overloaded signal, meaning there are variants of it, for
        # example the activated(int) variant emits the index of the chosen
        # option, rather than it's text
        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)

    def combo_chosen(self, text):
        """
        Handler called when a distro is chosen from the combo box
        """
        self.lbl.setText(text)


# If the program is run directly or passed as an argument to the python
# interpreter then create a ComboBoxBasic instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = ComboBoxBasic()
    gui.show()
    app.exec_()
