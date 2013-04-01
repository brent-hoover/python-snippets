"""Common geometry behaviors for Tk/Tix"""
import atexit, os, Tix as Tk

class GeomSaverMixin:
    """Mixin for widgets that save/load their geometry."""
    def __init__(self, title):
        self.title(title)
        atexit.register(self.save_geom)
        self.filename = '.tkgeom-%s' % title
        self.load_geom()

        self.bind("<Destroy>", self.save_geom)
    def get_full_filename(self):
        return os.path.join(os.environ['HOME'], self.filename)
    def load_geom(self, *args):
        try:
            f = file(self.get_full_filename(), 'r')
            geom = f.read()
            self.wm_geometry(geom)
        except:
            pass
    def save_geom(self, *args):
        try:
            geom = self.wm_geometry()
            f = file(self.get_full_filename(), 'w')
            f.write(geom)
        except Tk.TclError: # since we call this twice, we expect an error
                            # the second time
            pass

class ToplevelGeomSaver(Tk.Toplevel, GeomSaverMixin):
    """Just like a Toplevel, but title is necessary"""
    def __init__(self, master, title, *args, **kw):
        Tk.Toplevel.__init__(self, master, *args, **kw)
        GeomSaverMixin.__init__(self, title)

class TkRootGeomSaver(Tk.Tk, GeomSaverMixin):
    """Just like a Tk (root object), but title is necessary"""
    def __init__(self, title, *args, **kw):
        Tk.Tk.__init__(self, *args, **kw)
        GeomSaverMixin.__init__(self, title)

if __name__ == "__main__":
    root = TkRootGeomSaver('mr-root')
    t = ToplevelGeomSaver(root, 'hello')
    Tk.mainloop()
