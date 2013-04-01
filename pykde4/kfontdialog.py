#!/usr/bin/env python

# [SNIPPET_NAME: Dialog (Font Selection)]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: A dialog that provides interactive font selection]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KFontDialog.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel, QDialog, QFont

from PyKDE4.kdecore import i18n
from PyKDE4.kdeui import KVBox, KHBox, KPushButton, KFontDialog

helpText = """A KFontDialog allows the user to select a new font.

Click the button to change the font of the displayed text.
"""

quote = """Now is the winter of our discontent
made summer by this glorious sun of York.
"""

dialogName = "KFontDialog" 

class MainFrame(KVBox):       
    def __init__(self, parent):
        KVBox.__init__(self, parent)
        self.setSpacing (40)
        self.help = QLabel (i18n (helpText), self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)

        self.button = KPushButton(i18n("Show %s" % dialogName), self)
        self.button.setFixedSize (200, 30)
        self.layout ().setAlignment (self.button, Qt.AlignHCenter)
        self.fontLabel = QLabel (quote, self)
        self.layout ().setAlignment (self.fontLabel, Qt.AlignHCenter)
        
        self.connect(self.button, SIGNAL('clicked()'), self.showDialog)

    def showDialog(self):
        font = QFont ()
        result, checkState = KFontDialog.getFont (font)
        if result == QDialog.Accepted:
            self.fontLabel.setFont (font)



# This example can be run standalone

if __name__ == '__main__':

    import sys

    from PyQt4.QtCore import Qt
    from PyQt4.QtGui import QFrame, QVBoxLayout
    
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
