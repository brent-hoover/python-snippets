class PrettyClever(object):
    def __init__(self, *stuff):
        self.stuff = stuff
    def __getstate__(self):
        def normalize(x):
            if isinstance(x, file):
                return 1, (x.name, x.mode, x.tell())
            return 0, x
        return [ normalize(x) for x in self.stuff ]
    def __setstate__(self, stuff):
        def reconstruct(x):
            if x[0] == 0:
                return x[1]
            name, mode, offs = x[1]
            openfile = open(name, mode)
            openfile.seek(offs)
            return openfile
        self.stuff = tuple([reconstruct(x) for x in stuff])
