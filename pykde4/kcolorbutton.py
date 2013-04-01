#!/usr/bin/env python

# [SNIPPET_NAME: Pushbutton (Color Selection)]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: A pushbutton to display or allow user selection of a color]
# [SNIPPET_AUTHOR: Jim Bublitz <jbublitz@nwinternet.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KColorButton.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel

from PyKDE4.kdecore import i18n
from PyKDE4.kdeui import KVBox, KHBox, KColorButton, KColorCells, KColorCombo, KColorPatch

helpText = """These are examples of three ways of changing colors interactively,
and one widget that displays a chosen color.

When KColorButton is clicked, it pops up a color selection dialog.

KColorCells offers one way to present a pre-selected range of color
choices, and may have more rows and columns than displayed here.
Click on a cell to select a color.

KColorCombo provides a programmable drop down list of colors to select
from.

Finally, KColorPatch will display a specified color. In this example, using
any of the other three widgets to select a color will change the color of
the KColorPatch.
"""

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help  = QLabel (helpText, self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter)
        
        hBox1 = KHBox (self)
        hBox1.setSpacing (10)
        hBox1.setMargin (40)

        
        colorButtonLabel = QLabel ("KColorButton", hBox1)
        colorButton = KColorButton (hBox1)

        colorCellsLabel = QLabel ("KColorCells", hBox1)
        colorCells = KColorCells (hBox1, 1, 8)
        colorCells.setMaximumSize (160, 20)
        colorCells.setColor (0, Qt.black)
        colorCells.setColor (1, Qt.red)
        colorCells.setColor (2, Qt.yellow)
        colorCells.setColor (3, Qt.blue)
        colorCells.setColor (4, Qt.darkGreen)
        colorCells.setColor (5, Qt.magenta)
        colorCells.setColor (6, Qt.gray)
        colorCells.setColor (7, Qt.white)
        
        
        colorComboLabel = QLabel ("KColorCombo", hBox1)
        colorCombo = KColorCombo (hBox1)

        colorList = [Qt.black, Qt.red, Qt.yellow, Qt.blue, Qt.darkGreen, Qt.magenta, Qt.gray, Qt.white]
        colorCombo.setColors (colorList)
        colorCombo.setMaximumWidth (80)
        
        hBox2 = KHBox (self)
        hBox2.setSpacing (10)
        self.layout ().setAlignment (hBox2, Qt.AlignHCenter | Qt.AlignTop)
        self.setStretchFactor (hBox2, 1)
        
        colorPatchLabel = QLabel ("KColorPatch", hBox2)
        hBox2.layout ().setAlignment (colorPatchLabel, Qt.AlignHCenter)
        self.colorPatch = KColorPatch (hBox2)
        self.colorPatch.setFixedSize (40, 40)
        hBox2.layout ().setAlignment (self.colorPatch, Qt.AlignHCenter)

        self.colorPatch.setColor (Qt.red)
        self.colorPatch.show ()

        self.connect (colorButton, SIGNAL ("changed (const QColor&)"), self.colorPatch.setColor)
        self.connect (colorCells, SIGNAL ("colorSelected (int, const QColor&)"), self.colorCellSelected)
        self.connect (colorCombo, SIGNAL ("activated (const QColor&)"), self.colorPatch.setColor)
        
    def colorCellSelected (self, int, color):
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
