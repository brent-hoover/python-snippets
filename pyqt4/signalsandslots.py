#!/usr/bin/env python
#
# [SNIPPET_NAME: Connecting signals and slots]
# [SNIPPET_CATEGORIES: PyQt4]
# [SNIPPET_DESCRIPTION: Different ways to connect signals and slots]
# [SNIPPET_AUTHOR: Darren Worrall <dw@darrenworrall.co.uk>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html#connecting-disconnecting-and-emitting-signals]

# example signalsandslots.py

# In this example we will simulate some things that are done automatically
# if you are building your ui's with Qt Designer and the pyuic4 tools

import sys
from PyQt4 import QtGui, QtCore

class SignalsAndSlots(QtGui.QWidget):
    """
    A few signal and slot examples
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Signals and Slots')
        # Set the window dimensions
        self.resize(450,400)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a button which we will manually connect to a slot
        self.man_btn = QtGui.QPushButton('Manually connected', self)
        self.vbox.addWidget(self.man_btn)

        # Manually connect the clicked signal to it's handler, as we have done
        # in other examples
        self.connect(self.man_btn, QtCore.SIGNAL('clicked()'), self.manual_slot)
        
        # Create a button which we will automatially connect to a slot
        self.brokenbtn = QtGui.QPushButton("'Broken' Auto Button", self)
        # For autoconnection to work we have to call setobject name. When 
        # using the designer this is done automatially
        self.brokenbtn.setObjectName('brokenbtn')
        self.vbox.addWidget(self.brokenbtn)

        # Create a button which we will automatially connect to a slot, only
        # a bit more carefully :)
        self.workingbtn = QtGui.QPushButton("'Working' Auto Button", self)
        self.workingbtn.setObjectName('workingbtn')
        self.vbox.addWidget(self.workingbtn)

        # Finally a text edit area to show some results
        self.log_window = QtGui.QTextEdit()
        self.vbox.addWidget(self.log_window)
        # read only, sorry folks ;)
        self.log_window.setReadOnly(True)

        # Automatcally connect signals to slots by their name. This is also
        # done for you if you use the result of pyuic4, in the setupUi call
        QtCore.QMetaObject.connectSlotsByName(self)

    def manual_slot(self):
        """
        This slot/handlier is manually connected in __init__
        """
        # A manually connected slot, as pre previous examples. No drama :)
        msg = 'This slot was manually connected, and is called once'
        self.log_window.append(msg)

    def on_brokenbtn_clicked(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        # connectSlotsByName found this handler - it starts with on_, followed
        # by the object name, followed by the signal this should be connected
        # to. However, as you will see, it is called twice...
        msg = 'This slot was automatically connected, and is called twice'
        self.log_window.append(msg)

    @QtCore.pyqtSlot()     
    def on_workingbtn_clicked(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        # Using the same logic this slot is connected to the 'working' button
        # and only called once. The reason for this is that a lot of Qt signals
        # are overloaded, and if you dont specify which specific variant you
        # are interested in, then _all_ of them will be connected. Once way to
        # specify the specific signal is by use of the decorator above - in
        # this case, we will be connected to the signal with no arguments
        #
        # It is better explained in the documentation:
        # http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html#connecting-slots-by-name
        msg = 'This slot was automatically connected, and is called once'
        self.log_window.append(msg)



# If the program is run directly or passed as an argument to the python
# interpreter then create a SignalsAndSlots instance and show it
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = SignalsAndSlots()
    gui.show()
    app.exec_()
