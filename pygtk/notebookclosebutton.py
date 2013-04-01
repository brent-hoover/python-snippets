#!/usr/bin/env python
#
# [SNIPPET_NAME: Notebook close button]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Shows how to add a close button to a notebook tab]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_AUTHOR: Simon Vermeersch <simonvermeersch@gmail.com>]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtknotebook.html]

import gtk

class TestApp:
    def __init__(self):
        #Create a window
        w = gtk.Window()
        w.connect("destroy", lambda wid: gtk.main_quit())
        w.connect("delete_event", lambda a1,a2:gtk.main_quit())
        w.set_size_request(600, 400)
        
        #Create a notebook
        self.notebook = gtk.Notebook()
        w.add(self.notebook)
        
        #Add some example tabs
        for x in xrange(1, 10):
            self.create_tab("Tab" + str(x))
        
        #Show everything
        w.show_all()
        
    def create_tab(self, title):
        #hbox will be used to store a label and button, as notebook tab title
        hbox = gtk.HBox(False, 0)
        label = gtk.Label(title)
        hbox.pack_start(label)

        #get a stock close button image
        close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
        image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
        
        #make the close button
        btn = gtk.Button()
        btn.set_relief(gtk.RELIEF_NONE)
        btn.set_focus_on_click(False)
        btn.add(close_image)
        hbox.pack_start(btn, False, False)
        
        #this reduces the size of the button
        style = gtk.RcStyle()
        style.xthickness = 0
        style.ythickness = 0
        btn.modify_style(style)

        hbox.show_all()

        #the tab will have a single widget: a label
        widget = gtk.Label(title)
        
        #add the tab
        self.notebook.insert_page(widget, hbox)
        
        #connect the close button
        btn.connect('clicked', self.on_closetab_button_clicked, widget)

    def on_closetab_button_clicked(self, sender, widget):
        #get the page number of the tab we wanted to close
        pagenum = self.notebook.page_num(widget)
        #and close it
        self.notebook.remove_page(pagenum)
        
testapp = TestApp()
gtk.main()
