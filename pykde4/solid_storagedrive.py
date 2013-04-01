#!/usr/bin/env python

# [SNIPPET_NAME: Solid (Storage Drive)]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: Device integration framework for a storage drive]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/solid/index.html, http://api.kde.org/pykde-4.3-api/solid/Solid.StorageDrive.html]

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QSizePolicy, QTreeWidget, QTreeWidgetItem, QLabel

from PyKDE4.kdecore import i18n
from PyKDE4.solid import Solid
from PyKDE4.kdeui import KVBox, KHBox, KColorButton

helpText = """The Solid class discovers information about the hardware on a machine.

Solid.StorageDrive objects retrieve information about storage devices on a
machine. the table below shows the data for your machine.

We use Solid.Device.allDevices () to get a list of all devices, and then
filter it for Solid.StorageDrive types.
"""

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help  = QLabel (i18n (helpText), self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        self.setSpacing (10)
       
        hBox = KHBox (self)
       
        display = QTreeWidget (hBox)        
        display.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)
        display.setHeaderLabels (["Device", "Bus", "Type", "Hot Plug", "Removable"])
        display.setColumnWidth (0, 150)

        # convert enum values to strings for display
        bus2Str = {Solid.StorageDrive.Ide : "IDE",\
                   Solid.StorageDrive.Usb : "USB",\
                   Solid.StorageDrive. Ieee1394 : "IEE1394",\
                   Solid.StorageDrive.Scsi : "SCSI",\
                   Solid.StorageDrive.Sata : "SATA",\
                   Solid.StorageDrive.Platform : "Platform"
                  }


        driveType2Str = {Solid.StorageDrive.HardDisk : "Hard Disk",\
                         Solid.StorageDrive.CdromDrive : "CD ROM",\
                         Solid.StorageDrive.Floppy : "Floppy",\
                         Solid.StorageDrive.Tape : "Tape",\
                         Solid.StorageDrive.CompactFlash : "Compact Flash",\
                         Solid.StorageDrive.MemoryStick : "Memory Stick",\
                         Solid.StorageDrive.SmartMedia : "Smart Media",\
                         Solid.StorageDrive.SdMmc : "SD MMC",\
                         Solid.StorageDrive.Xd : "XD"
                        }
        

        # retrieve a list of Solid.Device for this machine
        deviceList = Solid.Device.allDevices ()

        # filter the list of all devices and display matching results
        # note that we never create a Solid.StorageDrive object, but
        # receive one from the call to 'asDeviceInterface'
        for device in deviceList:
            if device.isDeviceInterface (Solid.DeviceInterface.StorageDrive):
                drive = device.asDeviceInterface (Solid.DeviceInterface.StorageDrive)
                QTreeWidgetItem (display, [device.product (),
                                           bus2Str [drive.bus ()],
                                           driveType2Str [drive.driveType ()],
                                           str (drive.isHotpluggable ()),
                                           str (drive.isRemovable ())])

        
        

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
