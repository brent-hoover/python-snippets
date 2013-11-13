import re, os, glob
import win32api, win32con
def _getLocation():
    """ Examines the registry to find the cookie folder IE uses """
    key = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    regkey = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, key, 0,
        win32con.KEY_ALL_ACCESS)
    num = win32api.RegQueryInfoKey(regkey)[1]
    for x in range(num):
        k = win32api.RegEnumValue(regkey, x)
        if k[0] == 'Cookies':
            return k[1]
def _getCookieFiles(location, name):
    """ Rummages through cookie folder, returns filenames including `name'.
    `name' is normally the domain, e.g 'activestate' to get cookies for
    activestate.com (also e.g. for activestate.foo.com, but you can
    filter out such accidental hits later). """
    filemask = os.path.join(location, '*%s*' % name)
    return glob.glob(filemask)
def _findCookie(filenames, cookie_re):
    """ Look through a group of files for a cookie that satisfies a
    given compiled RE, returning first such cookie found, or None. """
    for file in filenames:
        data = open(file, 'r').read()
        m = cookie_re.search(data)
        if m: return m.group(1)
def findIECookie(domain, cookie):
    """ Finds the cookie for a given domain from IE cookie files """
    try:
        l = _getLocation()
    except Exception, err:
        # Print a debug message
        print "Error pulling registry key:", err
        return None
    # Found the key; now find the files and look through them
    f = _getCookieFiles(l, domain)
    if f:
        cookie_re = re.compile('%s\n(.*?)\n' % cookie)
        return _findCookie(f, cookie_re)
    else:
        print "No cookies for domain (%s) found" % domain
        return None
if __name__=='__main__':
    print findIECookie(domain='kuro5hin', cookie='k5-new_session')
