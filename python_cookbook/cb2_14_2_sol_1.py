import os, string
def isSSL():
    """ Return true if we are on an SSL (https) connection. """
    return os.environ.get('SSL_PROTOCOL', '') != ''
def getScriptname():
    """ Return the scriptname part of the URL ("/path/to/my.cgi"). """
    return os.environ.get('SCRIPT_NAME', '')
def getPathinfo():
    """ Return the remaining part of the URL. """
    pathinfo = os.environ.get('PATH_INFO', '')
    # Fix for a well-known bug in IIS/4.0
    if os.name == 'nt':
        scriptname = getScriptname()
        if pathinfo.startswith(scriptname):
            pathinfo = pathinfo[len(scriptname):]
    return pathinfo
def getQualifiedURL(uri=None):
    """ Return a full URL starting with schema, servername, and port.
        Specifying uri causes it to be appended to the server root URL
        (uri must then start with a slash).
    """
    schema, stdport = (('http', '80'), ('https', '443'))[isSSL()]
    host = os.environ.get('HTTP_HOST', '')
    if not host:
        host = os.environ.get('SERVER_NAME', 'localhost')
        port = os.environ.get('SERVER_PORT', '80')
        if port != stdport: host = host + ":" + port
    result = "%s://%s" % (schema, host)
    if uri: result = result + uri
    return result
def getBaseURL():
    """ Return a fully qualified URL to this script. """
    return getQualifiedURL(getScriptname())
