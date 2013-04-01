#!/usr/bin/env python
#
# [SNIPPET_NAME: Action Group]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Demonstrates using a gtk.ActionGroup.]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-NewInPyGTK2.4.html#sec-ActionsAndActionGroups, http://www.pygtk.org/docs/pygtk/class-gtkactiongroup.html]

import pygtk
pygtk.require('2.0')
import gtk

class ActionGroupExample:
    def __init__(self):
        # Create the toplevel window
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_size_request(300, -1)
        vbox = gtk.VBox()
        window.add(vbox)

        # Create an accelerator group
        accelgroup = gtk.AccelGroup()
        # Add the accelerator group to the toplevel window
        window.add_accel_group(accelgroup)

        # Create an ActionGroup named ActionExample
        actiongroup = gtk.ActionGroup('ActionGroupExample')
        self.actiongroup = actiongroup

        # Create a ToggleAction, etc.
        actiongroup.add_toggle_actions([('Mute', None, '_Mute', '<Control>m',
                                         'Mute the volume', self.mute_cb)])

        # Create actions
        actiongroup.add_actions([('Quit', gtk.STOCK_QUIT, '_Quit me!', None,
                                  'Quit the Program', self.quit_cb),
                                 ('File', None, '_File'),
                                 ('Sound', None, '_Sound'),
                                 ('RadioBand', None, '_Radio Band')])
        actiongroup.get_action('Quit').set_property('short-label', '_Quit')

        # Create some RadioActions
        actiongroup.add_radio_actions([('AM', None, '_AM', '<Control>a',
                                        'AM Radio', 0),
                                       ('FM', None, '_FM', '<Control>f',
                                        'FM Radio', 1),
                                       ('SSB', None, '_SSB', '<Control>s',
                                        'SSB Radio', 2),
                                       ], 0, self.radioband_cb)
        for action in actiongroup.list_actions():
            action.set_accel_group(accelgroup)

        # Create a MenuBar
        menubar = gtk.MenuBar()
        vbox.pack_start(menubar, False)

        # Create the File Action MenuItem
        file_menuitem = actiongroup.get_action('File').create_menu_item()
        menubar.append(file_menuitem)

        # Create the File Menu
        file_menu = gtk.Menu()
        file_menuitem.set_submenu(file_menu)

        # Create a Quit MenuItem
        quitaction = actiongroup.get_action('Quit')
        quititem = quitaction.create_menu_item()
        file_menu.append(quititem)

        # Create and populate the Sound menu with a Mute menuitem
        sound_menuitem = actiongroup.get_action('Sound').create_menu_item()
        menubar.append(sound_menuitem)
        sound_menu = gtk.Menu()
        sound_menuitem.set_submenu(sound_menu)
        muteaction = actiongroup.get_action('Mute')
        muteitem = muteaction.create_menu_item()
        sound_menu.append(muteitem)

        # Create and populate the RadioBand menu
        radiobanditem = actiongroup.get_action('RadioBand').create_menu_item()
        menubar.append(radiobanditem)
        radiobandmenu = gtk.Menu()
        radiobanditem.set_submenu(radiobandmenu)
        amaction = actiongroup.get_action('AM')
        amitem = amaction.create_menu_item()
        radiobandmenu.append(amitem)
        fmaction = actiongroup.get_action('FM')
        fmitem = fmaction.create_menu_item()
        radiobandmenu.append(fmitem)
        ssbaction = actiongroup.get_action('SSB')
        ssbitem = ssbaction.create_menu_item()
        radiobandmenu.append(ssbitem)

        # Create a Toolbar
        toolbar = gtk.Toolbar()
        vbox.pack_start(toolbar, False)

        # Create a proxy ToolItem
        quittoolitem = quitaction.create_tool_item()
        toolbar.insert(quittoolitem, 0)

        # Create a separator
        separator = gtk.SeparatorToolItem()
        toolbar.insert(separator, -1)

        # Create toggle and radio tool items and add to toolbar
        mutetoolitem = muteaction.create_tool_item()
        toolbar.insert(mutetoolitem, -1)
        separator = gtk.SeparatorToolItem()
        toolbar.insert(separator, -1)
        amtoolitem = amaction.create_tool_item()
        toolbar.insert(amtoolitem, -1)
        fmtoolitem = fmaction.create_tool_item()
        toolbar.insert(fmtoolitem, -1)
        ssbtoolitem = ssbaction.create_tool_item()
        toolbar.insert(ssbtoolitem, -1)

        # Create and pack two Labels
        label = gtk.Label('Sound is not muted')
        vbox.pack_start(label)
        self.mutelabel = label
        label = gtk.Label('Radio band is AM')
        vbox.pack_start(label)
        self.bandlabel = label

        # Create buttons to control visibility and sensitivity of actions
        buttonbox = gtk.HButtonBox()
        sensitivebutton = gtk.CheckButton('Sensitive')
        sensitivebutton.set_active(True)
        sensitivebutton.connect('toggled', self.toggle_sensitivity)
        visiblebutton = gtk.CheckButton('Visible')
        visiblebutton.set_active(True)
        visiblebutton.connect('toggled', self.toggle_visibility)
        # add them to buttonbox
        buttonbox.pack_start(sensitivebutton, False)
        buttonbox.pack_start(visiblebutton, False)
        vbox.pack_start(buttonbox)

        # Have to set tooltip after toolitems are added to toolbar
        for action in actiongroup.list_actions():
            action.set_property('tooltip', action.get_property('tooltip'))

        window.show_all()
        return

    def mute_cb(self, action):
        # action has not toggled yet
        text = ('muted', 'not muted')[action.get_active()==False]
        self.mutelabel.set_text('Sound is %s' % text)
        return

    def radioband_cb(self, action, current):
        text = ('AM', 'FM', 'SSB')[action.get_current_value()]
        self.bandlabel.set_text('Radio band is %s' % text)
        return

    def quit_cb(self, b):
        print 'Quitting program'
        gtk.main_quit()

    def toggle_sensitivity(self, b):
        self.actiongroup.set_sensitive(b.get_active())
        return

    def toggle_visibility(self, b):
        self.actiongroup.set_visible(b.get_active())
        return

if __name__ == '__main__':
    ba = ActionGroupExample()
    gtk.main()
