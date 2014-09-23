#File: Frame_2.py
#Author: Me
#Description: 
import wx
class MyFrame(wx.Frame):
    """docstring for MyFrame"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, -1, "Frame with Menu and Status", 
                        pos = (125, 10), size = (300, 100)) 
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        statusBar = self.CreateStatusBar()
        toolBar = self.CreateToolBar()
        toolBar.Realize()
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()