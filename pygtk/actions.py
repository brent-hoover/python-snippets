#!/usr/bin/env python
#
# [SNIPPET_NAME: Actions]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Demonstrates using Actions with a gtk.Action and gtk.AccelGroup]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/ch-NewInPyGTK2.4.html#sec-Actions, http://www.pygtk.org/docs/pygtk/class-gtkaction.html]

import pygtk
pygtk.require('2.0')
import gtk

class ActionExample:
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
        actiongroup = gtk.ActionGroup('ActionExample')

        # Create an action for quitting the program using a stock item
        quitaction = gtk.Action('Quit', '_Quit me!', 'Quit the Program',
                            gtk.STOCK_QUIT)
        quitaction.set_property('short-label', '_Quit')
        # Connect a callback to the action
        quitaction.connect('activate', self.quit_cb)

        # Add the action to the actiongroup with an accelerator
        # None means use the stock item accelerator
        actiongroup.add_action_with_accel(quitaction, None)

        # Have the action use accelgroup
        quitaction.set_accel_group(accelgroup)

        # Connect the accelerator to the action
        quitaction.connect_accelerator()

        # Create a ToggleAction, etc.
        muteaction = gtk.ToggleAction('Mute', '_Mute', 'Mute the volume', None)
        actiongroup.add_action_with_accel(muteaction, '<Control>m')
        muteaction.set_accel_group(accelgroup)
        muteaction.connect_accelerator()
        muteaction.connect('toggled', self.mute_cb)

        # Create some RadioActions
        amaction = gtk.RadioAction('AM', '_AM', 'AM Radio', None, 0)
        actiongroup.add_action_with_accel(amaction, '<Control>a')
        amaction.set_accel_group(accelgroup)
        amaction.connect_accelerator()
        amaction.set_active(True)

        fmaction = gtk.RadioAction('FM', '_FM', 'FM Radio', None, 1)
        actiongroup.add_action_with_accel(fmaction, '<Control>f')
        fmaction.set_accel_group(accelgroup)
        fmaction.connect_accelerator()
        fmaction.set_group(amaction)

        ssbaction = gtk.RadioAction('SSB', 'SS_B', 'Single Sideband Radio',
                                    None, 2)
        actiongroup.add_action_with_accel(ssbaction, '<Control>s')
        ssbaction.set_accel_group(accelgroup)
        ssbaction.connect_accelerator()
        ssbaction.connect('changed', self.radioband_cb)
        ssbaction.set_group(amaction)

        # Create a MenuBar
        menubar = gtk.MenuBar()
        vbox.pack_start(menubar, False)

        # Create the File Action and MenuItem
        file_action = gtk.Action('File', '_File', None, None)
        actiongroup.add_action(file_action)
        file_menuitem = file_action.create_menu_item()
        menubar.append(file_menuitem)

        # Create the File Menu
        file_menu = gtk.Menu()
        file_menuitem.set_submenu(file_menu)

        # Create a proxy MenuItem
        quititem = quitaction.create_menu_item()
        file_menu.append(quititem)

        # Create and populate the Sound menu with a Mute menuitem
        sound_action = gtk.Action('Sound', '_Sound', None, None)
        actiongroup.add_action(sound_action)
        sound_menuitem = sound_action.create_menu_item()
        menubar.append(sound_menuitem)
        sound_menu = gtk.Menu()
        sound_menuitem.set_submenu(sound_menu)
        muteitem = muteaction.create_menu_item()
        sound_menu.append(muteitem)

        # Create and populate the RadioBand menu
        radioband_action = gtk.Action('RadioBand', '_Radio Band', None, None)
        actiongroup.add_action(radioband_action)
        radioband_menuitem = radioband_action.create_menu_item()
        menubar.append(radioband_menuitem)
        radioband_menu = gtk.Menu()
        radioband_menuitem.set_submenu(radioband_menu)
        amitem = amaction.create_menu_item()
        radioband_menu.append(amitem)
        fmitem = fmaction.create_menu_item()
        radioband_menu.append(fmitem)
        ssbitem = ssbaction.create_menu_item()
        radioband_menu.append(ssbitem)

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

        # Create a button to use as another proxy widget
        quitbutton = gtk.Button()
        # add it to the window
        vbox.pack_start(quitbutton, False)

        # Connect the action to its proxy widget
        quitaction.connect_proxy(quitbutton)
        # Have to set tooltip after toolitems are added to toolbar
        for action in actiongroup.list_actions():
            action.set_property('tooltip', action.get_property('tooltip'))
        tooltips = gtk.Tooltips()
        tooltips.set_tip(quitbutton, quitaction.get_property('tooltip'))

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

if __name__ == '__main__':
    ba = ActionExample()
    gtk.main()
