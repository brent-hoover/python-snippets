#!/usr/bin/env python
#
# [SNIPPET_NAME: Count down timer]
# [SNIPPET_CATEGORIES: PyGTK, gobject]
# [SNIPPET_DESCRIPTION: Two examples of how to make a count down timer]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_AUTHOR: Simon Vermeersch <simonvermeersch@gmail.com>]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2reference/gobject-functions.html#function-gobject--timeout-add]

import gtk, gobject

class CounterApp:
    def __init__(self):
        self.w = gtk.Window()
        self.w.connect("destroy", lambda wid: gtk.main_quit())
        self.w.connect("delete_event", lambda a1,a2:gtk.main_quit())

        vbox = gtk.VBox()
        self.w.add(vbox)

        self.label = gtk.Label("Counter example")
        vbox.pack_start(self.label)

        hbox = gtk.HBox()
        vbox.pack_start(hbox)

        btn1 = gtk.Button("Method 1")
        btn1.connect("clicked", self.btn1_clicked)
        hbox.pack_start(btn1)

        btn2 = gtk.Button("Method 2")
        btn2.connect("clicked", self.btn2_clicked)
        hbox.pack_start(btn2)

        self.w.show_all()

    def btn1_clicked(self, sender):
        counter = 15
        while counter >= 0:
            gobject.timeout_add(counter * 1000, self.countdown_function_method1, 15-counter)
            counter -= 1

    def countdown_function_method1(self, counter):
        if counter > 0:
            self.label.set_text("Remaining: " + str(counter))
        else:
            self.label.set_text("All done!")

    def btn2_clicked(self, sender):
        self.counter = 15
        gobject.timeout_add(1000, self.countdown_function_method2)
        self.countdown_function_method2()

    def countdown_function_method2(self):
        if self.counter > 0:
            self.label.set_text("Remaining: " + str(self.counter))
            self.counter -= 1
            return True
        else:
            self.label.set_text("All done!")
            return False
if __name__ == "__main__":
    app = CounterApp()
    gtk.main()
