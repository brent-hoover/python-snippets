#!/usr/bin/env python
# [SNIPPET_NAME: Toggle Spelling]
# [SNIPPET_CATEGORIES: GtkSpell]
# [SNIPPET_DESCRIPTION: Toggle spelling on and off]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtkspell/class-gtkspell.html]
# [SNIPPET_LICENSE: GPL]

import pygtk
pygtk.require("2.0")
import gtkspell 
import gtk

global spell_toggle 
global text

def toggle(widget, data=None):
	global spell_toggle, text
        if spell_toggle:
                spell_toggle = 0
		spell = gtkspell.get_from_text_view (text)
                spell.detach()
        else:
                spell_toggle = 1
                spell = gtkspell.Spell (text)


def destroy(widget, data=None):
        gtk.main_quit()

print dir (gtkspell)
print dir (gtkspell.Spell)

spell_toggle = 1

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy", destroy)

vbox = gtk.VBox()
button = gtk.Button("toggle spelling")
button.connect("clicked", toggle, None)

text = gtk.TextView()
vbox.add (text)
vbox.add (button)

window.add (vbox)
spell = gtkspell.Spell (text)
spell.set_language ("en_US")

window.show_all()

gtk.main()

