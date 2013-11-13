import _winreg as wr
aReg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
targ = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
aKey = wr.OpenKey(aReg, targ, 0, wr.KEY_WRITE)
wr.DeleteValue(aKey, "MyNewKey")
wr.CloseKey(aKey)
wr.CloseKey(aReg)
