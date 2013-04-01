#!/usr/bin/env python
#
# [SNIPPET_NAME: Download a file asynchronously]
# [SNIPPET_CATEGORIES: GIO]
# [SNIPPET_DESCRIPTION: Download a file async (useful for not blocking the GUI)]
# [SNIPPET_AUTHOR: Jono Bacon <jono@ubuntu.com>]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygobject/class-giofile.html]
# [SNIPPET_LICENSE: GPL]

import gio, gtk, os

# Downloading a file in an async way is a great way of not blocking a GUI. This snippet will show a simple GUI and
# download the main HTML file from ubuntu.com without blocking the GUI. You will see the dialog appear with no content
# and when the content has downloaded, the GUI will be refreshed. This snippet also writes the content to the home
# directory as pythonsnippetexample-ubuntuwebsite.html.

# To download in an async way you kick off the download and when it is complete, another callback is called to process
# it (namely, display it in the window and write it to the disk). This separation means you can download large files and
# not block the GUI if needed. 

class Example(object):
    def download_file(self, data, url):
        """Download the file using gio"""

        # create a gio stream and download the URL passed to the method
        self.stream = gio.File(url)

        # there are two methods of downloading content: load_contents_async and read_async. Here we use load_contents_async as it
        # downloads the full contents of the file, which is what we want. We pass it a method to be called when the download has
        # complete: in this case, self.download_file_complete
        self.stream.load_contents_async(self.download_file_complete)

    def download_file_complete(self, gdaemonfile, result):
        """Method called after the file has downloaded"""

        # the result from the download is actually a tuple with three elements. The first element is the actual content
        # so let's grab that
        content = self.stream.load_contents_finish(result)[0]

        # update the label with the content
        label.set_text(content)

        # let's now save the content to the user's home directory
        outputfile = open(os.path.expanduser('~') + "/pythonsnippetexample-ubuntuwebsite.html","w")
        outputfile.write(content)

ex = Example()

dial = gtk.Dialog()
label = gtk.Label()
dial.action_area.pack_start(label)
label.show_all()
label.connect('realize', ex.download_file, "http://www.ubuntu.com")
dial.run()
