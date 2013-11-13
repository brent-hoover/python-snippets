from Tkinter import *
from ScrolledText import ScrolledText
from unicodedata import lookup
import os
class Diacritical(object):
    """ Mixin class that adds keyboard bindings for accented characters, plus
        other common functionality (e.g.: Control-A == 'select all' on Windows).
    """
    if os.name == "nt":
        stroke = '/'
    else:
        stroke = 'minus'
    accents = (('acute', "'"), ('grave', '`'), ('circumflex', '^'),
               ('tilde', '='), ('diaeresis', '"'), ('cedilla', ','),
               ('stroke', stroke))
    def __init__(self):
        # Fix some non-Windows-like Tk bindings, if we're on Windows
        if os.name == 'nt':
            self.bind("<Control-Key-a>", self.select_all)
            self.bind("<Control-Key-/>", lambda event: "break")
        # Diacritical bindings
        for a, k in self.accents:
            self.bind("<Control-Key-%s><Key>" % k,
                        lambda event, a=a: self.insert_accented(event.char, a))
    def insert_accented(self, c, accent):
        if c.isalpha():
            if c.isupper():
                cap = 'capital'
            else:
                cap = 'small'
            try:
                c = lookup("latin %s letter %c with %s" % (cap, c, accent))
                self.insert(INSERT, c)
                return "break"
            except KeyError, e:
                pass
class DiacriticalEntry(Entry, Diacritical):
    """ Tkinter Entry widget with some extra key bindings for
        entering typical Unicode characters - with umlauts, accents, etc. """
    def __init__(self, master=None, **kwargs):
        Entry.__init__(self, master=None, **kwargs)
        Diacritical.__init__(self)
    def select_all(self, event=None):
        self.selection_range(0, END)
        return "break"
class DiacriticalText(ScrolledText, Diacritical):
    """ Tkinter ScrolledText widget with some extra key bindings for
        entering typical Unicode characters - with umlauts, accents, etc. """
    def __init__(self, master=None, **kwargs):
        ScrolledText.__init__(self, master=None, **kwargs)
        Diacritical.__init__(self)
    def select_all(self, event=None):
        self.tag_add(SEL, "1.0", "end-1c")
        self.mark_set(INSERT, "1.0")
        self.see(INSERT)
        return "break"
