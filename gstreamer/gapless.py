
# [SNIPPET_NAME: Gapless playback]
# [SNIPPET_CATEGORIES: GStreamer]
# [SNIPPET_DESCRIPTION: Shows how to use gstreamer to play music without any gap between tracks ]
# [SNIPPET_AUTHOR: Simon Vermeersch <simonvermeersch@gmail.com>]
# [SNIPPET_LICENSE: GPL]

#!/usr/bin/python
import pygst
pygst.require("0.10")
import gst
import sys
import gobject

class Player:
    def __init__(self, filename):
        self.filename = filename
        
        #this only works with playbin2
        self.player = gst.element_factory_make("playbin2", "player")
        self.player.set_property("uri", filename)
        self.player.connect("about-to-finish", self.on_about_to_finish)

    def run(self):
        self.player.set_state(gst.STATE_PLAYING)
        loop = gobject.MainLoop()
        loop.run()

    def on_about_to_finish(self, player):
        #The current song is about to finish, if we want to play another
        #song after this, we have to do that now

        #we'll just repeat the song here as an example
        player.set_property("uri", self.filename)

if __name__ == "__main__":
    gobject.threads_init()
    player = Player("file:///usr/share/example-content/Ubuntu_Free_Culture_Showcase/InTheCircle.oga")
    player.run()

