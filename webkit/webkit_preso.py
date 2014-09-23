#!/usr/bin/env python
#
# [SNIPPET_NAME: Presenter]
# [SNIPPET_CATEGORIES: Webkit]
# [SNIPPET_DESCRIPTION: Fullscreen presenter program, for HTML presentations]
# [SNIPPET_AUTHOR: Akkana Peck <akkana@shallowsky.com>]
# [SNIPPET_DOCS: http://shallowsky.com/blog/programming/webkit-presenter.html]
# [SNIPPET_LICENSE: GPL]

import sys, os
import gtk, gobject
import webkit

class WebBrowser(gtk.Window):
    def __init__(self, url):
        gtk.Window.__init__(self)

        # Either run fullscreen, or set an initial window size
        #self.set_default_size(1024,768)
        self.fullscreen()

        self._browser= webkit.WebView()
        self.add(self._browser)
        self.connect('destroy', gtk.main_quit)

        self._browser.open(url)    # throw err if url isn't defined
        self.show_all()

if __name__ == "__main__":
    if len(sys.argv) <= 1 :
        print "Usage:", sys.argv[0], "url"
        sys.exit(0)

    # Figure out if it's a filename or a url
    url = sys.argv[1]
    if url.find(':') < 0 :
        # If it's a local file, it needs to be converted to an absolute URL
        if url[0] == '/' :
            url = 'file://' + url
        else :
            url = 'file://' + os.getcwd() + '/' + url

    gobject.threads_init()
    webbrowser = WebBrowser(url)
    gtk.main()

