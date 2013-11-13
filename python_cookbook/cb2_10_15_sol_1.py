from win32com.client import Dispatch
ShellWindowsCLSID = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
ShellWindows = Dispatch(ShellWindowsCLSID)
print '%d instances of IE' % len(shellwindows)
print
for shellwindow in ShellWindows :
    print shellwindow
    print shellwindos.LocationName
    print shellwindos.LocationURL
    print
