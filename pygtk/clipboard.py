#!/usr/bin/env python
#
# [SNIPPET_NAME: Clipboard]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Using the clipboard]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-NewInPyGTK2.2.html, http://www.pygtk.org/docs/pygtk/class-gtkclipboard.html]

import pygtk
pygtk.require('2.0')
import gtk, gobject

class ClipboardInfo:
    pass

class ClipboardExample:
    # update button label and tooltips
    def update_buttons(self):
        for i in range(len(self.clipboard_history)):
            info = self.clipboard_history[i]
            if info:
                button = self.buttons[i]
                if info.text:
                    button.set_label(' '.join(info.text[:16].split('\n')))
                if info.targets:
                    # put target info in button tootip
                    self.button_tips.set_tip(button, info.targets)
        return

    # singal handler called when clipboard returns target data
    def clipboard_targets_received(self, clipboard, targets, info):
        if targets:
            # have to remove dups since Netscape is broken
            targ = {}
            for t in targets:
                targ[str(t)] = 0
            targ = targ.keys()
            targ.sort()
            info.targets = '\n'.join(targ)
        else:
            info.targets = None
            print 'No targets for:', info.text
        self.update_buttons()
        return

    # signal handler called when the clipboard returns text data
    def clipboard_text_received(self, clipboard, text, data):
        if not text or text == '':
            return
        cbi = ClipboardInfo()
        cbi.text = text
        # prepend and remove duplicate
        history = [info for info in self.clipboard_history
                   if info and info.text<>text]
        self.clipboard_history = ([cbi] + history)[:self.num_buttons]
        self.clipboard.request_targets(self.clipboard_targets_received, cbi)
        return

    # display the clipboard history text associated with the button
    def clicked_cb(self, button):
        i = self.buttons.index(button)
        if self.clipboard_history[i]:
            self.textbuffer.set_text(self.clipboard_history[i].text)
        else:
            self.textbuffer.set_text('')
        return

    # get the clipboard text
    def fetch_clipboard_info(self):
        self.clipboard.request_text(self.clipboard_text_received)
        return True

    def set_clipboard(self, button):
        text = self.textbuffer.get_text(*self.textbuffer.get_bounds())
        self.clipboard.set_text(text)
        return

    def __init__(self):
        self.num_buttons = 10
        self.buttons = self.num_buttons * [None]
        self.clipboard_history = self.num_buttons * [None]
        self.window = gtk.Window()
        self.window.set_title("Clipboard Example")
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_border_width(0)
        vbbox = gtk.VButtonBox()
        vbbox.show()
        vbbox.set_layout(gtk.BUTTONBOX_START)
        hbox = gtk.HBox()
        hbox.pack_start(vbbox, False)
        hbox.show()
        self.button_tips = gtk.Tooltips()
        for i in range(self.num_buttons):
            self.buttons[i] = gtk.Button("---")
            self.buttons[i].set_use_underline(False)
            vbbox.pack_start(self.buttons[i])
            self.buttons[i].show()
            self.buttons[i].connect("clicked", self.clicked_cb)
        vbox = gtk.VBox()
        vbox.show()
        scrolledwin = gtk.ScrolledWindow()
        scrolledwin.show()
        self.textview = gtk.TextView()
        self.textview.show()
        self.textview.set_size_request(200,100)
        self.textview.set_wrap_mode(gtk.WRAP_CHAR)
        self.textbuffer = self.textview.get_buffer()
        scrolledwin.add(self.textview)
        vbox.pack_start(scrolledwin)
        button = gtk.Button('Copy to Clipboard')
        button.show()
        button.connect('clicked', self.set_clipboard)
        vbox.pack_start(button, False)
        hbox.pack_start(vbox)
        self.window.add(hbox)
        self.window.show()
        self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
        self.clipboard.request_text(self.clipboard_text_received)
        gobject.timeout_add(1500, self.fetch_clipboard_info)
        return

def main():
  gtk.main()
  return 0

if __name__ == '__main__':
    cbe = ClipboardExample()
    main()
