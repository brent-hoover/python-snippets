#!/usr/bin/env python

# [SNIPPET_NAME: Solid (Network Interface)]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: Device integration framework for a network interface]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/solid/index.html, http://api.kde.org/pykde-4.3-api/solid/Solid.NetworkInterface.html]

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QSizePolicy, QTreeWidget, QTreeWidgetItem, QLabel

from PyKDE4.kdecore import i18n
from PyKDE4.solid import Solid, Solid
from PyKDE4.kdeui import KVBox, KHBox, KTextEdit

helpText = """The Solid class discovers information about the hardware on a machine.

Solid.NetworkInterface objects retrieve information about the network
on a machine.

We use Solid.Device.allDevices () to get a list of all devices, and then
filter it for Solid.NetworkInterface types.
"""

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help  = QLabel (i18n (helpText), self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        self.setSpacing (10)

        statusString = {
                          Solid.Networking.Unknown: "Unknown",\
                          Solid.Networking.Unconnected: "Unconnected",\
                          Solid.Networking.Disconnecting: "Disconnecting",\
                          Solid.Networking.Connecting: "Connecting",\
                          Solid.Networking.Connected: "Connected"\
                       }

        status = Solid.Networking.status ()
        self.label = QLabel ("Status:   %s" % statusString [status], self)
        
        hBox = KHBox (self)
                
        display = QTreeWidget (hBox)
        display.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)
        display.setHeaderLabels (["Interface", "Name", "Wireless", "HW Addr", "MAC Addr"])
        display.setColumnWidth (0, 200)
        display.setColumnWidth (1, 75)
        display.setColumnWidth (3, 150)

        # retrieve a list of Solid.Device for this machine
        deviceList = Solid.Device.allDevices ()

        
        # filter the list of all devices and display matching results
        # note that we never create a Solid.NetworkInterface object, but
        # receive one from the 'asDeviceInterface' call
        for device in deviceList:
            if device.isDeviceInterface (Solid.DeviceInterface.NetworkInterface):
                iface = device.asDeviceInterface (Solid.DeviceInterface.NetworkInterface)
                QTreeWidgetItem (display, [device.product (),
                                           iface.ifaceName (),
                                           str (iface.isWireless ()),
                                           iface.hwAddress (),
                                           str (iface.macAddress ())])

        
        

# This example can be run standalone

if __name__ == '__main__':

    import sys

    from PyQt4.QtCore import SIGNAL
    
    from PyKDE4.kdecore import KCmdLineArgs, KAboutData, KLocalizedString, ki18n
    from PyKDE4.kdeui import KApplication, KMainWindow
    
    
    class MainWin (KMainWindow):
        def __init__ (self, *args):
            KMainWindow.__init__ (self)

            self.resize(640, 480)
            self.setCentralWidget (MainFrame (self))
    
    
    #-------------------- main ------------------------------------------------
    
    appName     = "Solid_StorageDrive"
    catalog     = ""
    programName = ki18n ("Solid_StorageDrive")                 #ki18n required here
    version     = "1.0"
    description = ki18n ("Solid.StorageDrive Example")         #ki18n required here
    license     = KAboutData.License_GPL
    copyright   = ki18n ("(c) 2007 Jim Bublitz")    #ki18n required here
    text        = ki18n ("none")                    #ki18n required here
    homePage    = "www.riverbankcomputing.com"
    bugEmail    = "jbublitz@nwinternet.com"

    aboutData   = KAboutData (appName, catalog, programName, version, description,
                              license, copyright, text, homePage, bugEmail)

    # ki18n required for first two addAuthor () arguments
    aboutData.addAuthor (ki18n ("Troy Melhase"), ki18n ("original concept"))
    aboutData.addAuthor (ki18n ("Jim Bublitz"), ki18n ("pykdedocs"))
    
    KCmdLineArgs.init (sys.argv, aboutData)
    
    app = KApplication ()
    mainWindow = MainWin (None, "main window")
    mainWindow.show()
    app.connect (app, SIGNAL ("lastWindowClosed ()"), app.quit)
    app.exec_ ()
