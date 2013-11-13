from Tkinter import *
class LabeledEntry(Entry):
    """ An Entry widget with an attached Label """
    def __init__(self, master=None, **kw):
        ekw = {}                               # Entry options dictionary
        fkw = {}                               # Frame options dictionary
        lkw = {'name':'label'}                 # Label options dictionary
        skw = {'padx':0, 'pady':0, 'fill':'x', # Geometry manager opts dict
                'side':'left'}
        fmove = ('name',)                      # Opts to move to the Frame dict
        lmove = ('text', 'textvariable',
                 'anchor','bitmap', 'image')   # Opts to move to the Label dict
        smove = ('side', 'padx', 'pady',       # Opts to move to the Geometry
                 'fill')                       # manager dictionary
        # dispatch each option towards the appropriate component
        for k, v in kw:
            if k in fmove: fkw[k] = v
            elif k in lmove: lkw[k] = v
            elif k in smove: skw[k] = v
            else: ekw[k] = v
        # make all components with the accumulated options
        self.body = Frame(master, **fkw)
        self.label = Label(self.body, **lkw)
        self.label.pack(side='left', fill=skw['fill'],
                        padx=skw['padx'], pady=skw['pady'])
        Entry.__init__(self, self.body, **ekw)
        self.pack(side=skw['side'], fill=skw['fill'],
                  padx=skw['padx'], pady=skw['pady'])
        methods = (Pack.__dict__.keys() +  # Set Frame geometry methods to self
                   Grid.__dict__.keys() +
                   Place.__dict__.keys())
        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.body, m))
