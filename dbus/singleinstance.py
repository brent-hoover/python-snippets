#!/usr/bin/env python
#
# [SNIPPET_NAME: Single Instance]
# [SNIPPET_CATEGORIES: dbus, PyGTK]
# [SNIPPET_DESCRIPTION: This small snippet shows how to use dbus to only limit a single instance running of your app]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_AUTHOR: Simon Vermeersch <simonvermeersch@gmail.com>]

import gtk
import gobject
import dbus, dbus.service, dbus.glib


class MainApp:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(350, 350)
        self.label = gtk.Label("label")
        
        self.window.add(self.label)
        self.window.show_all()
        
        self.window.connect("destroy", self.destroy)
        
    def destroy(self, sender):
        gtk.main_quit()

class ExampleService(dbus.service.Object):
    def __init__(self, app):
        self.app = app
        bus_name = dbus.service.BusName('org.example.Sample', bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/example/Sample')

    @dbus.service.method(dbus_interface='org.example.Sample')
    def show_window(self):
        self.app.window.present()
        
if __name__ == "__main__":
    if dbus.SessionBus().request_name("org.example.Sample") != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
        print "application already running"
        method = dbus.SessionBus().get_object("org.example.Sample", "/org/example/Sample").get_dbus_method("show_window")
        method()
    else:
        print "running application"
        app = MainApp()
        service = ExampleService(app)
        gtk.main()
