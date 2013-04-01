#!/usr/bin/env python

# [SNIPPET_NAME: Main Window Application]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: PyKDE4 example showing KMainWindow and KApplication]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KApplication.html, http://api.kde.org/pykde-4.3-api/kdeui/KMainWindow.html]

import sys

from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs
from PyKDE4.kdeui import KApplication, KMainWindow

from PyQt4.QtGui import QLabel

runner = True
        
helpText = """This short program is the basic KDE application.

It uses KAboutData to initialize some basic program information
that is used by KDE (beyond simply setting up the About dialog
box in a more complex program).

It creates a KMainWindow, so the program has a place to display
its output and interact with users.

It also creates a KApplication object, which is necessary for
the use of most KDE widgets and other classes, and makes
available access to standard information about things like
icons, directory locations, colors, fonts and similar data.

Lastly, it starts an event loop (app.exec_) to allow a user
to interact with the program.

Click the button to launch the application.
"""        



class MainWindow (KMainWindow):
    def __init__ (self):
        KMainWindow.__init__ (self)

        self.resize (640, 480)
        label = QLabel ("This is a simple PyKDE4 program", self)
        label.setGeometry (10, 10, 200, 20)

#--------------- main ------------------
if __name__ == '__main__':

    appName     = "KApplication"
    catalog     = ""
    programName = ki18n ("KApplication")
    version     = "1.0"
    description = ki18n ("KApplication/KMainWindow/KAboutData example")
    license     = KAboutData.License_GPL
    copyright   = ki18n ("(c) 2007 Jim Bublitz")
    text        = ki18n ("none")
    homePage    = "www.riverbankcomputing.com"
    bugEmail    = "jbublitz@nwinternet.com"
    
    aboutData   = KAboutData (appName, catalog, programName, version, description,
                                license, copyright, text, homePage, bugEmail)
    
        
    KCmdLineArgs.init (sys.argv, aboutData)
        
    app = KApplication ()
    mainWindow = MainWindow ()
    mainWindow.show ()
    app.exec_ ()
