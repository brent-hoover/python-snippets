import urllib
def isContentType(URLorFile, contentType='text'):
    """ Tells whether the URL (or pseudofile from urllib.urlopen) is of
        the required content type (default 'text').
    """
    try:
        if isinstance(URLorFile, str):
            thefile = urllib.urlopen(URLorFile)
        else:
            thefile = URLorFile
        result = thefile.info().getmaintype() == contentType.lower()
        if thefile is not URLorFile:
            thefile.close()
    except IOError:
        result = False    # if we couldn't open it, it's of _no_ type!
    return result
