# To use wxPython and Twisted together, do the following, in exact order:
import wx
from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor
# Then, have whatever other imports as may be necessary to your program
from twisted.web import xmlrpc, server
class MyFrame(wx.Frame):
    ''' Main window for this wx application. '''
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition,
                 size=(200, 100), style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
    def OnCloseWindow(self, event):
        self.Destroy()
        reactor.stop()
class MyXMLRPCApp(wx.App, xmlrpc.XMLRPC):
    ''' We're a wx Application _AND_ an XML-RPC server too. '''
    def OnInit(self):
        ''' wx-related startup code: builds the GUI. '''
        self.frame = MyFrame(None, -1, 'Hello')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True
    # methods exposed to XML-RPC clients:
    def xmlrpc_stop(self):
        """ Closes the wx application. """
        self.frame.Close()
        return 'Shutdown initiated'
    def xmlrpc_title(self, x):
        """ Change the wx application's window's caption. """
        self.frame.SetTitle(x)
        return 'Title set to %r' % x
    def xmlrpc_add(self, x, y):
        """ Provide some computational services to clients. """
        return x + y
if __name__ == '__main__':
    # pass False to emit stdout/stderr to shell, not an additional wx window
    app = MyXMLRPCApp(False)
    # Make the wx application twisted-aware
    reactor.registerWxApp(app)
    # Make a XML-RPC Server listening to port 7080
    reactor.listenTCP(7080, server.Site(app))
    # Start both reactor parts (wx MainLoop and XML-RPC server)
    reactor.run()
