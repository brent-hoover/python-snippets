#!/usr/bin/env python
#
# [SNIPPET_NAME: MessageDialog]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Explore MessageDialog options]
# [SNIPPET_AUTHOR: mac9416 <mac9416@keryxproject.org>]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygtk/class-gtkmessagedialog.html]
# [SNIPPET_LICENSE: GPL]

# example messagedialog.py

import pygtk
pygtk.require('2.0')
import gtk

class MessageDialogLauncher:
    def __init__(self):
        # self.options will be a dict storing {option names: option_widgets}
        self.options = {}

        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("MessageDialog Launcher")

        # It's a good idea to do this for all windows.
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2: gtk.main_quit())

        # Sets the border width of the window.
        self.window.set_border_width(10)

        vbox = gtk.VBox()
        self.window.add(vbox)

        # Start adding options to the interface.
        new_opts = add_options(vbox, 
                               'flags', 
                               ('gtk.DIALOG_MODAL', 
                                'gtk.DIALOG_DESTROY_WITH_PARENT'), 
                               gtk.CheckButton)
        self.options.update(new_opts)

        new_opts = add_options(vbox, 
                               'type', 
                               ('gtk.MESSAGE_INFO', 
                                'gtk.MESSAGE_WARNING', 
                                'gtk.MESSAGE_QUESTION', 
                                'gtk.MESSAGE_ERROR'), 
                               gtk.RadioButton)
        self.options.update(new_opts)

        new_opts = add_options(vbox, 
                               'buttons', 
                               ('gtk.BUTTONS_NONE', 
                                'gtk.BUTTONS_OK', 
                                'gtk.BUTTONS_CLOSE', 
                                'gtk.BUTTONS_CANCEL', 
                                'gtk.BUTTONS_YES_NO', 
                                'gtk.BUTTONS_OK_CANCEL'), 
                               gtk.RadioButton)
        self.options.update(new_opts)

        # Add a place to enter the message_format.
        title = 'message_format'
        vb = gtk.VBox()
        title_label = gtk.Label(title)
        vb.pack_start(title_label)
        title_label.show()
        message_format_entry = gtk.Entry()
        vb.pack_start(message_format_entry)
        message_format_entry.show()
        vbox.pack_start(vb)
        vb.show()
        self.options.update({title: message_format_entry})

        # Add a separator to keep things organized.
        hseparator = gtk.HSeparator()
        vbox.pack_start(hseparator)
        hseparator.show()

        # Add a button to launch the MessageDialog.
        btn = gtk.Button('Launch my MessageDialog!')
        btn.connect('clicked', self.on_message_dialog)
        vbox.pack_start(btn)
        btn.show()

        vbox.show()
        self.window.show()

    def on_message_dialog(self, widget, data=None):
        self.new_message_dialog(self.options)

    def new_message_dialog(self, options):
        """Launch a MessageDialog using the given options."""
        flags = []
        the_type = buttons = message_format = ''
        
        for opt, widget in options.iteritems():
            if type(widget) in (gtk.CheckButton, gtk.RadioButton):
                value = widget.get_active()
            elif type(widget) == gtk.Entry:
                value = widget.get_text()
            # Flags
            if opt == 'gtk.DIALOG_MODAL' and value:
                flags.append(opt)
            elif opt == 'gtk.DIALOG_DESTROY_WITH_PARENT' and value:
                flags.append(opt)
            # Type
            elif opt == 'gtk.MESSAGE_INFO' and value:
                the_type = gtk.MESSAGE_INFO
            elif opt == 'gtk.MESSAGE_WARNING' and value:
                the_type = gtk.MESSAGE_WARNING
            elif opt == 'gtk.MESSAGE_QUESTION' and value:
                the_type = gtk.MESSAGE_QUESTION
            elif opt == 'gtk.MESSAGE_ERROR' and value:
                the_type = gtk.MESSAGE_ERROR
            # Buttons
            elif opt == 'gtk.BUTTONS_NONE' and value:
                buttons = gtk.BUTTONS_NONE
            elif opt == 'gtk.BUTTONS_OK' and value:
                buttons = gtk.BUTTONS_OK
            elif opt == 'gtk.BUTTONS_CLOSE' and value:
                buttons = gtk.BUTTONS_CLOSE
            elif opt == 'gtk.BUTTONS_CANCEL' and value:
                buttons = gtk.BUTTONS_CANCEL
            elif opt == 'gtk.BUTTONS_YES_NO' and value:
                buttons = gtk.BUTTONS_YES_NO
            elif opt == 'gtk.BUTTONS_OK_CANCEL' and value:
                buttons = gtk.BUTTONS_OK_CANCEL
            elif opt == 'message_format':
                message_format = value

        if len(flags) == 2:
            flags = gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT
        elif flags == ['gtk.DIALOG_MODAL']:
            flags = gtk.DIALOG_MODAL
        elif flags == ['gtk.DIALOG_DESTROY_WITH_PARENT']:
            flags = gtk.DIALOG_DESTROY_WITH_PARENT
        else:
            flags = 0

        the_dialog = gtk.MessageDialog(self.window, flags, the_type, buttons, 
                                       message_format)
        result = the_dialog.run()
        the_dialog.destroy()

        if result == gtk.RESPONSE_NONE:
            print 'No response.'
        elif result in (gtk.RESPONSE_OK, gtk.RESPONSE_YES, gtk.RESPONSE_OK):
            print 'Response affirmative.'
        elif result in (gtk.RESPONSE_CLOSE, gtk.RESPONSE_NO, gtk.RESPONSE_CANCEL):
            print 'Response negative.'


def add_options(parent_box, title, options, kind):
    """Adds a title and options (checkbutton or radiobutton) to parent_box.
       Returns a dict of {option_names: widgets}.
       Hints:
        parent_box - a box to contain the options
        title - a string describing the kind of options
        options - a list of option names
        kind - gtk.CheckButton or gtk.RadioButton, whichever is appropriate
    """
    # options_dict will store {option_names: option_widgets}
    # The option_widgets will be used to access the widgets' values.
    option_dict = {}

    # First, set up the vbox and add the title.
    vbox = gtk.VBox()
    title_label = gtk.Label(title)
    vbox.pack_start(title_label)

    # Now add each option.
    group = None  # To begin with, we'll have no button and therefore no group.
    for option in options:
        if kind == gtk.RadioButton:
            if group:
                button = gtk.RadioButton(group, option, False)
            else:
                group = button = gtk.RadioButton(None, option, False)
        elif kind == gtk.CheckButton:
            button = gtk.CheckButton(option, False)
        vbox.pack_start(button)
        button.show()
        option_dict.update({option: button})

    # Wrap things up.
    parent_box.pack_start(vbox)
    title_label.show()
    vbox.show()

    return option_dict


def main():
    gtk.main()
    return 0   
  

if __name__ == "__main__":
    MessageDialogLauncher()
    main()

