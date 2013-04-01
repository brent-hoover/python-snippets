#!/usr/bin/env python

# [SNIPPET_NAME: Date Selection Widget]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: Provides a widget for calendar date input]
# [SNIPPET_AUTHOR: Troy Melhase]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/kdeui/KDatePicker.html]

from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QLabel

from PyKDE4.kdecore import i18n
from PyKDE4.kdeui import KVBox, KHBox, KDatePicker, KDateWidget


helpText = """Date selection widgets - KDatePicker and KDateWidget - provide widgets for calendar
date input.

KDatePicker emits two types of signals, either dateSelected() or dateEntered().

A line edit allows the user to select a date directly by entering numbers like
19990101 or 990101 into KDatePicker."""

class MainFrame(KVBox):
    def __init__(self, parent=None):
        KVBox.__init__(self, parent)
        self.help = QLabel (i18n (helpText), self)
        self.layout ().setAlignment (self.help, Qt.AlignHCenter | Qt.AlignTop)
        self.setSpacing (40)

        hBox  = KHBox (self)
        vBox1 = KVBox (hBox)
        vBox2 = KVBox (hBox)

        hBox.layout ().setAlignment (vBox1, Qt.AlignHCenter)
        hBox.layout ().setAlignment (vBox2, Qt.AlignHCenter)
        vBox1.setMargin (20)
        vBox2.setSpacing (20)
        
        self.datePickerLabel = QLabel ("KDatePicker", vBox1)

        self.datePicker = KDatePicker(vBox2)
        self.datePicker.setFixedSize (400, 200)

        self.other = QLabel('KDateWidget', vBox1)
        vBox1.layout ().setAlignment (self.other, Qt.AlignBottom)
        
        self.dateDisplay = KDateWidget(vBox2)

        
        self.connect(self.datePicker, SIGNAL('dateChanged(QDate)'),
                     self.dateDisplay.setDate)


# This example can be run standalone

if __name__ == '__main__':

    import sys
    
    from PyKDE4.kdecore import KCmdLineArgs, KAboutData, KLocalizedString, ki18n
    from PyKDE4.kdeui import KApplication, KMainWindow
    
                
    class MainWin (KMainWindow):
        def __init__ (self, *args):
            KMainWindow.__init__ (self)

            self.resize(640, 500)
            self.setCentralWidget (MainFrame (self))
    
    #-------------------- main ------------------------------------------------
    
    appName     = "kdatepicker"
    catalog     = ""
    programName = ki18n ("kdatepicker")
    version     = "1.0"
    description = ki18n ("KDatePicker Example")
    license     = KAboutData.License_GPL
    copyright   = ki18n ("(c) 2006 Troy Melhase")
    text        = ki18n ("none")
    homePage    = "www.riverbankcomputing.com"
    bugEmail    = "jbublitz@nwinternet.com"

    aboutData   = KAboutData (appName, catalog, programName, version, description,
                              license, copyright, text, homePage, bugEmail)

    aboutData.addAuthor (ki18n ("Troy Melhase"), ki18n ("original concept"))
    aboutData.addAuthor (ki18n ("Jim Bublitz"), ki18n ("pykdedocs"))
    
    KCmdLineArgs.init (sys.argv, aboutData)
    
    app = KApplication ()
    mainWindow = MainWin (None, "main window")
    mainWindow.show()
    app.connect (app, SIGNAL ("lastWindowClosed ()"), app.quit)
    app.exec_ ()
