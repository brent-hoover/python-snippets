#!/usr/bin/env python

# [SNIPPET_NAME: Dialog (Color Selection)]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: A color selection dialog]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KColorDialog.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QColor

from PyKDE4.kdecore import i18n
from PyKDE4.kdeui import KVBox, KHBox, KPushButton, KColorDialog, KColorPatch

helpText = """This example uses KColorDialog.getColor (color, parent) to
popup a dialog that allows the user to set the color of the KColorPatch
next to the button.

Click the button to run the dialog and select a color.
"""

dialogName = "KColorDialog" 

class MainFrame(KVBox):       
    def __init__(self, parent):
        KVBox.__init__(self, parent)
        self.help = QLabel (helpText, self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        
        hBox = KHBox (self)
        self.button = KPushButton(i18n("Show %s" % dialogName), hBox)
        self.button.setMaximumSize (250, 30)
        
        self.connect(self.button, SIGNAL('clicked()'), self.showDialog)

        self.colorPatch = KColorPatch (hBox)
        self.colorPatch.setColor (Qt.red)
        self.colorPatch.setMaximumSize (40, 40)


    def showDialog(self):
        color = QColor ()
        result = KColorDialog.getColor (color, self)
        self.colorPatch.setColor (color)



# This example can be run standalone

if __name__ == '__main__':

    import sys

    from PyKDE4.kdecore import KCmdLineArgs, KAboutData, KLocalizedString, ki18n
    from PyKDE4.kdeui import KApplication, KMainWindow
    
            
    class MainWin (KMainWindow):
        def __init__ (self, *args):
            KMainWindow.__init__ (self)

            self.resize(640, 480)
            self.setCentralWidget (MainFrame (self))    
    
    #-------------------- main ------------------------------------------------
    
    appName     = "default.py"
    catalog     = ""
    programName = ki18n ("default")                 #ki18n required here
    version     = "1.0"
    description = ki18n ("Default Example")         #ki18n required here
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
