import _winreg as wr
aReg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
try:
    targ = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
    print "*** Reading from", targ, "***"
    aKey = wr.OpenKey(aReg, targ)
    try:
        for i in xrange(1024):
            try:
                n, v, t = wr.EnumValue(aKey, i)
                print i, n, v, t
            except EnvironmentError:
                print "You have", i, "tasks starting at logon"
                break
    finally:
        wr.CloseKey(aKey)
    print "*** Writing to", targ, "***"
    aKey = wr.OpenKey(aReg, targ, 0, wr.KEY_WRITE)
    try:
        try:
            wr.SetValueEx(aKey, "MyNewKey", 0, REG_SZ, r"c:\winnt\explorer.exe")
        except EnvironmentError:
            print "Encountered problems writing into the Registry..."
            raise
    finally:
        CloseKey(aKey)
finally:
    CloseKey(aReg)
