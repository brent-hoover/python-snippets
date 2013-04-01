#!/usr/bin/env python

# [SNIPPET_NAME: About Application Dialog]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: PyKDE4 example showing the About application dialog]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdecore/KAboutData.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel, QSizePolicy

from PyKDE4.kdecore import i18n, ki18n, KAboutData
from PyKDE4.kdeui import KVBox, KHBox, KPushButton, KAboutApplicationDialog

helpText = """The KAboutApplicationDialog is normally displayed from the
applications Help menu.

It requires a KAboutData object to provide the information displayed in
the dialog. This is usually the same KAboutData object constructed when
you start your program, although a different object could be used.

Press the button below to display the dialog.
"""

dialogName = "KAboutApplicationDialog" 

appName     = "kaboutapplicationdialog.py"
catalog     = ""
programName = ki18n ("kaboutapplicationdialog")                 #ki18n required here
version     = "1.0"
description = ki18n ("KAboutApplicationDialog Example")         #ki18n required here
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


class MainFrame(KVBox):       
    def __init__(self, parent):
        KVBox.__init__(self, parent)
        self.help = QLabel (helpText, self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        
        hBox = KHBox (self)
        self.button = KPushButton(i18n("Show %s" % dialogName), hBox)
        self.button.setMaximumSize (250, 30)
        
        self.connect(self.button, SIGNAL('clicked()'), self.showDialog)

    def showDialog(self):
        dlg = KAboutApplicationDialog (aboutData, self.parent ())
        dlg.exec_ ()      



# This example can be run standalone

if __name__ == '__main__':

    import sys

    from PyQt4.QtCore import SIGNAL
    
    from PyKDE4.kdecore import KCmdLineArgs, KAboutData, KLocalizedString, ki18n
    from PyKDE4.kdeui import KApplication, KMainWindow
    
                
    class MainWin (KMainWindow):
        def __init__ (self, *args):
            KMainWindow.__init__ (self)

            self.resize (640, 480)           
            self.setCentralWidget (MainFrame (self))
    
    
    #-------------------- main ------------------------------------------------
    
    
    KCmdLineArgs.init (sys.argv, aboutData)
    
    app = KApplication ()
    mainWindow = MainWin (None, "main window")
    mainWindow.show()
    app.connect (app, SIGNAL ("lastWindowClosed ()"), app.quit)
    app.exec_ ()
