#!/usr/bin/env python

# [SNIPPET_NAME: Combo Box]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: An enhanced combo box which is a combined button, line-edit and popup list widget]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KComboBox.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel

from PyKDE4.kdecore import i18n, KStandardDirs
from PyKDE4.kdeui import KVBox, KHBox, KComboBox, KListWidget

helpText = """
KListWidget and KComboBox are useful for displaying or
interacting with lists of items. In this case, we
display the KStandardDirs file types and directory
locations.

KComboBox is filled from the QStringList that the
method "allTypes()" returns. It can also be filled
with a single item at a time, and we can sort or
add/remove items later. KDE has specialized KComboBox
subclasses for other purposes. It inherits methods
from QComboBox

KListWidget also displays lists of information, but all
are visible at the same time. It inherits classes
from QListWidget and QListView.
"""

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help  = QLabel (i18n (helpText), self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        self.setSpacing (10)
        
        hBox          = KHBox (self)
        self.layout ().setAlignment (hBox, Qt.AlignHCenter)
        
        cBox          = KVBox (hBox)
        hBox.layout ().setAlignment (cBox, Qt.AlignTop)
        hBox.setSpacing (25)
        hBox.setMargin (10)

        self.stdDirs  = KStandardDirs ()
        types         = self.stdDirs.allTypes ()
        
        comboLbl      = QLabel ("Types", cBox)
        combo         = KComboBox (cBox)        
        combo.addItems (types)
        cBox.layout ().setAlignment (comboLbl, Qt.AlignTop)
        cBox.layout ().setAlignment (combo, Qt.AlignTop)
        
        self.connect (combo, SIGNAL ("currentIndexChanged (const QString&)"), self.slotIndexChanged)

        lBox          = KVBox (hBox)
        listLbl       = QLabel ("Directories", lBox)
        self.location = KListWidget (lBox)
        self.location.setMaximumSize (400, 200)
        lBox.layout ().setAlignment (listLbl, Qt.AlignTop)
        lBox.layout ().setAlignment (self.location, Qt.AlignTop)

        self.slotIndexChanged (combo.currentText ())


    def slotIndexChanged (self, s):
        self.location.clear ()
        self.location.insertItems (0, self.stdDirs.resourceDirs (str (s)))

        


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
    
    appName     = "default"
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
