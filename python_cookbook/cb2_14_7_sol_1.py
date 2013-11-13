import os.path, urllib2
from urllib2 import urlopen, Request
COOKIEFILE = 'cookies.lwp'   # "cookiejar" file for cookie saving/reloading
# first try getting the best possible solution, cookielib:
try:
    import cookielib
except ImportError:                 # no cookielib, try ClientCookie instead
    cookielib = None
    try:
        import ClientCookie
    except ImportError:             # nope, no cookies today
        cj = None                   # so, in particular, no cookie jar
    else:                           # using ClientCookie, prepare everything
        urlopen = ClientCookie.urlopen
        cj = ClientCookie.LWPCookieJar()
        Request = ClientCookie.Request
else:                               # we do have cookielib, prepare the jar
    cj = cookielib.LWPCookieJar()
# Now load the cookies, if any, and build+install an opener using them
if cj is not None:
    if os.path.isfile(COOKIEFILE):
        cj.load(COOKIEFILE)
    if cookielib:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    else:
        opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cj))
        ClientCookie.install_opener(opener)
# for example, try a URL that sets a cookie
theurl = 'http://www.diy.co.uk'
txdata = None  # or, for POST instead of GET, txdata=urrlib.urlencode(somedict)
txheaders =  {'User-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
try:
    req = Request(theurl, txdata, txheaders)  # create a request object
    handle = urlopen(req)                     # and open it
except IOError, e:
    print 'Failed to open "%s".' % theurl
    if hasattr(e, 'code'):
        print 'Error code: %s.' % e.code
else:
    print 'Here are the headers of the page:'
    print handle.info()
# you can also use handle.read() to get the page, handle.geturl() to get the
# the true URL (could be different from `theurl' if there have been redirects)
if cj is None:
    print "Sorry, no cookie jar, can't show you any cookies today"
else:
    print 'Here are the cookies received so far:'
    for index, cookie in enumerate(cj):
        print index, ': ', cookie
    cj.save(COOKIEFILE)                     # save the cookies again
