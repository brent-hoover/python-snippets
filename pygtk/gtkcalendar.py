#!/usr/bin/env python
#
# [SNIPPET_NAME: Calendar]
# [SNIPPET_CATEGORIES: PyGTK]
# [SNIPPET_DESCRIPTION: Create a calendar widget]
# [SNIPPET_DOCS: http://www.pygtk.org/pygtk2tutorial/sec-Calendar.html, http://www.pygtk.org/docs/pygtk/class-gtkcalendar.html]

# example calendar.py
#
# Copyright (C) 1998 Cesar Miquel, Shawn T. Amundson, Mattias Gronlund
# Copyright (C) 2000 Tony Gale
# Copyright (C) 2001-2004 John Finlay
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import pygtk
pygtk.require('2.0')
import gtk, pango
import time

class CalendarExample:
    DEF_PAD = 10
    DEF_PAD_SMALL = 5
    TM_YEAR_BASE = 1900

    calendar_show_header = 0
    calendar_show_days = 1
    calendar_month_change = 2 
    calendar_show_week = 3

    def calendar_date_to_string(self):
        year, month, day = self.window.get_date()
        mytime = time.mktime((year, month+1, day, 0, 0, 0, 0, 0, -1))
        return time.strftime("%x", time.localtime(mytime))

    def calendar_set_signal_strings(self, sig_str):
        prev_sig = self.prev_sig.get()
        self.prev2_sig.set_text(prev_sig)

        prev_sig = self.last_sig.get()
        self.prev_sig.set_text(prev_sig)
        self.last_sig.set_text(sig_str)

    def calendar_month_changed(self, widget):
        buffer = "month_changed: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_day_selected(self, widget):
        buffer = "day_selected: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_day_selected_double_click(self, widget):
        buffer = "day_selected_double_click: %s"
        buffer = buffer % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

        year, month, day = self.window.get_date()

        if self.marked_date[day-1] == 0:
            self.window.mark_day(day)
            self.marked_date[day-1] = 1
        else:
            self.window.unmark_day(day)
            self.marked_date[day-1] = 0

    def calendar_prev_month(self, widget):
        buffer = "prev_month: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_next_month(self, widget):
        buffer = "next_month: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_prev_year(self, widget):
        buffer = "prev_year: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_next_year(self, widget):
        buffer = "next_year: %s" % self.calendar_date_to_string()
        self.calendar_set_signal_strings(buffer)

    def calendar_set_flags(self):
        options = 0
        for i in range(5):
            if self.settings[i]:
                options = options + (1<<i)
        if self.window:
            self.window.display_options(options)

    def calendar_toggle_flag(self, toggle):
        j = 0
        for i in range(5):
            if self.flag_checkboxes[i] == toggle:
                j = i

        self.settings[j] = not self.settings[j]
        self.calendar_set_flags()

    def calendar_font_selection_ok(self, button):
        self.font = self.font_dialog.get_font_name()
        if self.window:
            font_desc = pango.FontDescription(self.font)
            if font_desc: 
                self.window.modify_font(font_desc)

    def calendar_select_font(self, button):
        if not self.font_dialog:
            window = gtk.FontSelectionDialog("Font Selection Dialog")
            self.font_dialog = window
    
            window.set_position(gtk.WIN_POS_MOUSE)
    
            window.connect("destroy", self.font_dialog_destroyed)
    
            window.ok_button.connect("clicked",
                                     self.calendar_font_selection_ok)
            window.cancel_button.connect_object("clicked",
                                                lambda wid: wid.destroy(),
                                                self.font_dialog)
        window = self.font_dialog
        if not (window.flags() & gtk.VISIBLE):
            window.show()
        else:
            window.destroy()
            self.font_dialog = None

    def font_dialog_destroyed(self, data=None):
        self.font_dialog = None

    def __init__(self):
        flags = [
            "Show Heading",
            "Show Day Names",
            "No Month Change",
            "Show Week Numbers",
            ]
        self.window = None
        self.font = None
        self.font_dialog = None
        self.flag_checkboxes = 5*[None]
        self.settings = 5*[0]
        self.marked_date = 31*[0]

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Calendar Example")
        window.set_border_width(5)
        window.connect("destroy", lambda x: gtk.main_quit())

        window.set_resizable(False)

        vbox = gtk.VBox(False, self.DEF_PAD)
        window.add(vbox)

        # The top part of the window, Calendar, flags and fontsel.
        hbox = gtk.HBox(False, self.DEF_PAD)
        vbox.pack_start(hbox, True, True, self.DEF_PAD)
        hbbox = gtk.HButtonBox()
        hbox.pack_start(hbbox, False, False, self.DEF_PAD)
        hbbox.set_layout(gtk.BUTTONBOX_SPREAD)
        hbbox.set_spacing(5)

        # Calendar widget
        frame = gtk.Frame("Calendar")
        hbbox.pack_start(frame, False, True, self.DEF_PAD)
        calendar = gtk.Calendar()
        self.window = calendar
        self.calendar_set_flags()
        calendar.mark_day(19)
        self.marked_date[19-1] = 1
        frame.add(calendar)
        calendar.connect("month_changed", self.calendar_month_changed)
        calendar.connect("day_selected", self.calendar_day_selected)
        calendar.connect("day_selected_double_click",
                         self.calendar_day_selected_double_click)
        calendar.connect("prev_month", self.calendar_prev_month)
        calendar.connect("next_month", self.calendar_next_month)
        calendar.connect("prev_year", self.calendar_prev_year)
        calendar.connect("next_year", self.calendar_next_year)

        separator = gtk.VSeparator()
        hbox.pack_start(separator, False, True, 0)

        vbox2 = gtk.VBox(False, self.DEF_PAD)
        hbox.pack_start(vbox2, False, False, self.DEF_PAD)
  
        # Build the Right frame with the flags in 
        frame = gtk.Frame("Flags")
        vbox2.pack_start(frame, True, True, self.DEF_PAD)
        vbox3 = gtk.VBox(True, self.DEF_PAD_SMALL)
        frame.add(vbox3)

        for i in range(len(flags)):
            toggle = gtk.CheckButton(flags[i])
            toggle.connect("toggled", self.calendar_toggle_flag)
            vbox3.pack_start(toggle, True, True, 0)
            self.flag_checkboxes[i] = toggle

        # Build the right font-button 
        button = gtk.Button("Font...")
        button.connect("clicked", self.calendar_select_font)
        vbox2.pack_start(button, False, False, 0)

        #  Build the Signal-event part.
        frame = gtk.Frame("Signal events")
        vbox.pack_start(frame, True, True, self.DEF_PAD)

        vbox2 = gtk.VBox(True, self.DEF_PAD_SMALL)
        frame.add(vbox2)
  
        hbox = gtk.HBox (False, 3)
        vbox2.pack_start(hbox, False, True, 0)
        label = gtk.Label("Signal:")
        hbox.pack_start(label, False, True, 0)
        self.last_sig = gtk.Label("")
        hbox.pack_start(self.last_sig, False, True, 0)

        hbox = gtk.HBox (False, 3)
        vbox2.pack_start(hbox, False, True, 0)
        label = gtk.Label("Previous signal:")
        hbox.pack_start(label, False, True, 0)
        self.prev_sig = gtk.Label("")
        hbox.pack_start(self.prev_sig, False, True, 0)

        hbox = gtk.HBox (False, 3)
        vbox2.pack_start(hbox, False, True, 0)
        label = gtk.Label("Second previous signal:")
        hbox.pack_start(label, False, True, 0)
        self.prev2_sig = gtk.Label("")
        hbox.pack_start(self.prev2_sig, False, True, 0)

        bbox = gtk.HButtonBox ()
        vbox.pack_start(bbox, False, False, 0)
        bbox.set_layout(gtk.BUTTONBOX_END)

        button = gtk.Button("Close")
        button.connect("clicked", lambda w: gtk.main_quit())
        bbox.add(button)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()

        window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    CalendarExample()
    main()
