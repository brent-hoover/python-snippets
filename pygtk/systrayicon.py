#!/usr/bin/python
# -*- coding: utf-8 -*-

# [SNIPPET_NAME: Systray icon]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Shows a system tray icon with a menu  ]
# [SNIPPET_AUTHOR: João Pinto <joao.pinto@getdeb.net>]
# [SNIPPET_LICENSE: GPL]
#


import gtk


class SystrayIconApp:
	def __init__(self):
		self.tray = gtk.StatusIcon()
		self.tray.set_from_stock(gtk.STOCK_ABOUT) 
		self.tray.connect('popup-menu', self.on_right_click)
		self.tray.set_tooltip(('Sample tray app'))
		

    	def on_right_click(self, icon, event_button, event_time):
		self.make_menu(event_button, event_time)

    	def make_menu(self, event_button, event_time):
		menu = gtk.Menu()

		# show about dialog
		about = gtk.MenuItem("About")
		about.show()
		menu.append(about)
		about.connect('activate', self.show_about_dialog)

		# add quit item
		quit = gtk.MenuItem("Quit")
		quit.show()
		menu.append(quit)
		quit.connect('activate', gtk.main_quit)

		menu.popup(None, None, gtk.status_icon_position_menu,
		           event_button, event_time, self.tray)

	def  show_about_dialog(self, widget):
		about_dialog = gtk.AboutDialog()
		about_dialog.set_destroy_with_parent (True)
		about_dialog.set_icon_name ("SystrayIcon")
		about_dialog.set_name('SystrayIcon')
		about_dialog.set_version('0.1')
		about_dialog.set_copyright("(C) 2010 João Pinto")
		about_dialog.set_comments(("Program to demonstrate a system tray icon"))
		about_dialog.set_authors(['João Pinto <joao.pinto@getdeb.net>'])
		about_dialog.run()
		about_dialog.destroy()

if __name__ == "__main__":
	SystrayIconApp()
	gtk.main()
   

