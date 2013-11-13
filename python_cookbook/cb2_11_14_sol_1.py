from wxPython.wx import *
class MainFrame(wxFrame):
    #
    # snipped: mainframe class attributes
    #
    def __init__(self, parent, id, title):
        #
        # snipped: frame-specific initialization
        #
        # Create the notebook object
        self.nb = wxNotebook(self, -1,
            wxPoint(0,0), wxSize(0,0), wxNB_FIXEDWIDTH)
        # Populate the notebook with pages (panels), each driven by a
        # separate Python module which gets imported for the purpose:
        panel_names = "First Panel", "Second Panel", "The Third One"
        panel_scripts = "panel1", "panel2", "panel3"
        for name, script in zip(panel_names, panel_scripts):
            # Make panel named 'name' (driven by script 'script'.py)
            self.module = __import__(script, globals())
            self.window = self.module.runPanel(self, self.nb)
            if self.window: self.nb.AddPage(self.window, name)
        #
        # snipped: rest of frame initialization
        #
