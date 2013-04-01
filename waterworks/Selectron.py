"""The Selectron 6000 - A selecting widget for Tix.

The widget is modelled after the song selector in
xmms when you press the 'j' key.  The Selectron, unlike the one in xmms,
holds objects and relies on their __str__() method to display them in
the widget (you can change which method is used).

Filtering is done incrementally in the background.  Unless someone can
find me red-black tree augmented with order statistics information,
this is probably about as fast as it can run.  First, it filters the
items on screen, then it does a larger sweep.  If the query changes,
it stops filtering and the new filtering begins.

Note that many things are pretty static:  You can't change the objects
list or change the description of an object already in the list (yet).
Descriptions are cached for speed.

If you have the shellwords module, it will use that to split the text
entry.  Shellwords is available from 

http://www.crazy-compilers.com/py-lib/shellwords.html

It will let you type in quoted substrings:
"Hello there" hi hola ==> ['Hello there', 'hi', 'hola']

If you dont' have it, you will get:
"Hello there" hi hola ==> ['"Hello', 'there"', 'hi', 'hola']
"""

from Tix import *
import time

__author__ = 'David McClosky (dmcc+py AT bigasterisk DOT com)'
__version__ = '1.0'
__all__ = ['Selectron']

# TODO: 
#   right clicking copies description to entry
#   more documentation

# try to use shellwords, if not, fall back to a basic text splitter
have_shellwords = 0
try:
    import shellwords
    have_shellwords = 1
    def splitter_func(text):
        """Function to chop up a piece of text (shellwords version).
        Returns a list of pieces."""
        text = text.strip()
        try:
            return shellwords.shellwords(text)
        except shellwords.UnmatchedDoubleQuoteError:
            return shellwords.shellwords(text + '"')
        except shellwords.UnmatchedSingleQuoteError:
            return shellwords.shellwords(text + "'")
except ImportError:
    def splitter_func(text):
        """Function to chop up a piece of text (plain version).
        Returns a list of pieces."""
        return text.split()

class Selectron(Frame):
    """Various elements are configurable:
        master is the Tk master.  If you've done any Tk programming,
            you'll know what this is.  If not, you might want to learn
            Tk first.  Simply put, master is the parent of this widget
            and will probably be a Frame or a Tk object, but ymmv.
        exportselection and selectmode are forwarded to the listbox.
        browsecmd is called whenever someone changes their selection
            with a list of all the selected objects.
        command is called whenever they complete their selection by
            pressing enter in the entry widget.
        objects is the most important option.  It is a list of objects to
            display in the Selectron.
        sort is whether the objects should be sorted by description.
        flashcolor is the color that the cursor and vertical scrollbar
            will change to while filtering.
        method is the method to use to stringify objects.  __str__ is the
            default. XXX out of date

    Additionally, after initialization, you may further configure it.
    If you do 'sel = Selectron()':

        sel.list      The ScrolledListBox
        sel.listbox   The ScrolledListBox's listbox (this is a shortcut)
        sel.entry     The Entry
        sel.entryvar  The Entry's StringVar
        sel.oldcursorbg, sel.oldsbcolor
                      Copies of the colors of the cursor color in the
                      entry and vertical scrollbar.  If you change those,
                      you'll have to change these as well.  Sorry,
                      I can't think of a better way to do this for now.
            
    You can also read from sel.filtering to see if the widget is currently
    filtering."""
    def __init__(self, master, exportselection=0, selectmode=BROWSE,
                 browsecmd=None, command=None, objects=None, sort=1, 
                 flashcolor='red', method=str, case_sensitive=1):
        Frame.__init__(self, master)
        self.master = master
        self.method = method
        self.sort = sort
        self.selectcommand = command
        self.browsecommand = browsecmd
        self.flashcolor = flashcolor
        self.case_sensitive = case_sensitive

        if objects is None:
            self.objects = []
        else:
            self.objects = objects

        if sort:
            self.objects.sort()

        self.descs = {}
        for obj in self.objects:
            desc = self.method(obj)
            self.descs[obj] = desc

        # Tk guts
        self.list = ScrolledListBox(self, browsecmd=self.listbrowse_cb,
            command=self.object_picked)
        self.list.listbox.configure(exportselection=exportselection,
                                    selectmode=selectmode) # I hate these things
        self.list.pack(expand=1, fill=BOTH)
        self.bind("<Key>", self.forward_key) # send keys to Entry
        self.list.bind("<Key>", self.forward_key) # send keys to Entry
        self.list.listbox.bind("<Key>", self.forward_key)
        self.listbox = self.list.listbox
        # self.listbox.selection_set(0)

        self.entryvar = StringVar()
        self.entry = Entry(self, textvariable=self.entryvar)
        self.entry.pack(expand=0, fill=X)
        self.entryvar.trace('w', self.got_input)
        self.entry.focus()
        self.entry.bind("<Return>", self.object_picked)

        # Forward these keys from the entry to listbox.
        # borrowed from skim (http://bigasterisk.com/skim)
        bindings = {
            # some emacs bindings
            '<Control-n>' : ('yview', (SCROLL, 1, UNITS)),
            '<Control-p>' : ('yview', (SCROLL, -3, UNITS)),
            '<Control-v>' : ('yview', (SCROLL, 1, PAGES)),
            '<Alt-v>' :     ('yview', (SCROLL, -1, PAGES)),

            # these should actually be just forwarded as keysyms
            # '<Up>' :        ('yview', (SCROLL, -2, UNITS)),
            # '<Down>' :      ('yview', (SCROLL, 2, UNITS)),

            '<Next>' :      ('yview', (SCROLL, 1, PAGES)),
            '<Prior>' :     ('yview', (SCROLL, -1, PAGES)),

            '<Home>' :      ('yview', (MOVETO, 0)),
            '<End>' :       ('yview', (MOVETO, 1)),
        }

        for k, cb in bindings.items():
            self.entry.bind(k, lambda evt, cb=cb: self.scroll(*cb))

        # save old colors for cursor and scrollbar
        self.oldcursorbg = self.entry['insertbackground']
        self.oldsbcolor = self.list.vsb['bg']

        self.sel_objects = self.objects[:]
        self.last_input = ''
        self.last_parse = ['']
        self.last_input_time = None
        self.filtering = 0

        self.populate_list()
    def scroll(self, fn, args=None, kw=None):
        """Help with some listbox scrolling functions"""
        if not args: args = ()
        if not kw: kw = {}
        fns = {
            'xview' : self.listbox.xview,
            'yview' : self.listbox.yview,
        }
        apply(fns[fn], args, kw)
    def populate_list(self):
        """Clears the list and then readds all the objects"""
        self.listbox.delete(0, END)
        for obj in self.objects:
            self.listbox.insert(END, self.descs[obj])

        self.sel_objects = self.objects[:]
    def get_visible_range(self):
        """Returns the indices of the visible objects in the listbox:
        (start, end)"""
        visible_start_px = self.listbox.winfo_vrooty()
        visible_end_px = visible_start_px + self.listbox.winfo_vrootheight()

        return (self.listbox.nearest(visible_start_px), 
                self.listbox.nearest(visible_end_px))
    def indicate_filter_start(self):
        """Called when filtering is started"""
        self.entry['insertbackground'] = self.flashcolor
        self.list.vsb['bg'] = self.flashcolor
        self.filtering = 1
    def indicate_filter_end(self):
        """Called when filtering is finished"""
        self.entry['insertbackground'] = self.oldcursorbg
        self.list.vsb['bg'] = self.oldsbcolor
        self.filtering = 0
    def filter_visible(self, substrings, timekey):
        """Start a filter for all items visible in the listbox"""
        if timekey == self.last_input_time:
            changed = 1
            while changed:
                vstart, vend = self.get_visible_range()
                newstart, newend, changed = \
                    self.filter_indices(substrings, vstart, vend)
    def filter_start(self, substrings, timekey):
        """This function is called whenever the entry query changes.  It
        filters the visible area then the rest."""
        self.indicate_filter_start()
        if self.sel_objects:
            def filter():
                self.filter_visible(substrings, timekey)

                index = len(self.sel_objects)
                self.filter_list_bg(substrings, 0, index, timekey)
                
            # don't start filtering immediately, since they might type more
            self.master.after(5, filter)
    def filter_indices(self, substrings, start, end, count=20):
        """Filter up to count items from start to end for the query substring"""
        changes = 0
        for iteration in range(count):
            end -= 1
            if end < start: 
                break

            obj = self.sel_objects[end]
            if not self.match(obj, substrings):
                changes = 1
                self.sel_objects.remove(obj)
                self.listbox.delete(end)

        else: # if break is not reached, i.e. if there are more to do
            return (start, end, changes)

        # no more work to do
        return (-1, -1, changes)

    def filter_list_bg(self, substrings, start, end, timekey, count=20, rate=5):
        """Start a new filtering job from start to end, filtering up to
        count objects and resting for rate milliseconds.  The timekey
        should be the result of time.time().  Filtering will stop if
        the entry has been changed since filtering started."""
        if timekey == self.last_input_time:
            start, end, changed = self.filter_indices(substrings, start, end)
            if start != -1: # if more work needs to be done
                self.master.after(rate, lambda: self.filter_list_bg(substrings, 
                            start, end, timekey, count))
            else:
                self.indicate_filter_end()

    def forward_key(self, event):
        """Forward keys from the listbox to the entry"""
        keysym = event.keysym

        if keysym == 'BackSpace':
            current = self.entry.index(INSERT)
            self.entry.delete(current - 1, current)
        elif keysym == 'Delete':
            self.entry.focus()
            current = self.entry.index(INSERT)
            self.entry.delete(current, current + 1)
        elif keysym in ('Right', 'Left'):
            current = self.entry.index(INSERT)
            self.entry.focus()
            if keysym == 'Right':
                newindex = current + 1
            else:
                newindex = current - 1
            self.entry.icursor(newindex)
        elif keysym in ('Up', 'Down', 'Prior', 'Next'):
            # XXX fix this junk up
            # print "forwarding up"
            # pass # nothing to do here
            self.listbox.focus()
            # if not self.listbox.curselection():
                # self.listbox.selection_set(0)
        elif keysym == 'Return':
            self.object_picked()
        elif event.char == '': # I think we don't care about any more of these
            pass
            # print "You didn't account for a keysym", event.keysym
        else:
            self.entry.insert(INSERT, event.char)
    def got_input(self, *args):
        """The callback function for the entry.  This will initiate new 
        filtering jobs if necessary.  Old ones will die automagically.  If
        the user deletes a key, we have to repopulate the listbox, 
        unfortunately.  We also try to maintain their current view but we can't
        restore the selection when they delete."""

        new_input = self.entryvar.get()
        parse = splitter_func(new_input)
        if parse == self.last_parse:
            return
        self.last_input_time = time.time()

        if not self.case_sensitive:
            parse = [s.lower() for s in parse]

        last_len = len(self.last_input)
        new_len = len(new_input)
        if last_len < new_len and new_input.find('-') == -1:
            self.filter_start(parse, timekey=self.last_input_time)
        else:
            # maintain their current viewpoint by re-see-ing to the object
            # in the middle of their screen
            vstart, vend = self.get_visible_range()

            if len(self.sel_objects):
                first_obj = self.sel_objects[(vstart + vend) / 2]
            else:
                first_obj = None

            self.populate_list()
            if first_obj:
                try:
                    self.listbox.see(self.sel_objects.index(first_obj))
                except IndexError:
                    pass

            if new_len:
                self.filter_start(parse, timekey=self.last_input_time)
        self.last_input = new_input
        self.last_parse = parse
    def match(self, obj, substrings):
        """Return whether a specific object contains each of the substrings"""
        desc = self.descs[obj]

        if not self.case_sensitive:
            desc = desc.lower()

        for sub in substrings:
            if sub[0] == '-':
                sub = sub[1:]
                if sub and desc.find(sub) != -1:
                    return 0
            else:
                if desc.find(sub) == -1:
                    return 0
        else:
            return 1
    def listbrowse_cb(self, *args):
        """This calls the browsecommand callback if one is defined"""
        if self.browsecommand:
            indexes = self.listbox.curselection()
            try:
                objects = [self.sel_objects[int(item)] for item in indexes]
            except ValueError: 
                pass

            self.browsecommand(objects)
    def object_picked(self, *args):
        """This calls the command callback"""
        indexes = self.listbox.curselection()
        try:
            objects = [self.sel_objects[int(item)] for item in indexes]
        except ValueError: 
            pass

        if not self.listbox.curselection():
            objects = self.sel_objects
        self.selectcommand(objects)

if __name__ == '__main__': # a demo
    def mr_browser(*args):
        print "mr_browse", args
    def mr_command(*args):
        print "mr_command", args

    print "opening words..."
    objects=open("/usr/share/dict/words").readlines()
    print "cleaning up..."
    import random
    random.shuffle(objects)
    objects = objects[:1000]
    objects = [obj.strip() for obj in objects]
    print "done"
    
    root = Tk()
    root.title("The Selectron 6000")
    selectron = Selectron(root, sort=1, objects=objects, 
                          command=mr_command, browsecmd=mr_browser,
                          selectmode=EXTENDED, case_sensitive=0)
    selectron.pack(expand=1, fill=BOTH)

    mainloop()
