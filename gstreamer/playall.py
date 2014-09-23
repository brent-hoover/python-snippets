
# [SNIPPET_NAME: Playing a Pipeline]
# [SNIPPET_CATEGORIES: GStreamer]
# [SNIPPET_DESCRIPTION: Construct and play a pipeline]
# [SNIPPET_AUTHOR: Tiago Boldt Sousa <tiagoboldt@gmail.com>]
# [SNIPPET_LICENSE: GPL]


#!/usr/bin/python

import pygst
pygst.require("0.10")
import gst
import sys
import gobject

#Create a player

class Player:
	def __init__(self, file):
		#Element playbin automatic plays any file
		self.player = gst.element_factory_make("playbin", "player")
		#Set the uri to the file
		self.player.set_property("uri", "file://" + file)

		#Enable message bus to check for errors in the pipeline
		bus = self.player.get_bus()
		bus.add_signal_watch()
		bus.connect("message", self.on_message)

	
	def run(self):
		self.player.set_state(gst.STATE_PLAYING)

	def on_message(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS:
			#file ended, stop
			self.player.set_state(gst.STATE_NULL)
			loop.quit()
		elif t == gst.MESSAGE_ERROR:
			#Error ocurred, print and stop
			self.player.set_state(gst.STATE_NULL)
			err, debug = message.parse_error()
			print "Error: %s" % err, debug
			loop.quit()

#Execution starts here

#Specify your file bellow 
#It can be any video/audio supported by gstreamer
file = "/usr/share/sounds/gnome/default/alerts/bark.ogg"

player = Player(file)
player.run()
loop = gobject.MainLoop()
loop.run()

