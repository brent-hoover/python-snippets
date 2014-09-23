#!/usr/bin/env python
#
# [SNIPPET_NAME: Webkit Button]
# [SNIPPET_CATEGORIES: Webkit, PyGTK]
# [SNIPPET_DESCRIPTION: Shows how to create a link, "button", inside HTMl and have webkit pass that to gtk]
# [SNIPPET_AUTHOR: Andy Breiner <breinera@gmail.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: https://wiki.ubuntu.com/MeetingLogs/OpWeek1003/Webkit]

# A version of the program was presented by Ryan Paul during Opportunistic
# Developer Week

import gtk, webkit, webbrowser
import gobject

class Button:
    default_site = "http://search.yahoo.com/"

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        # Create the threads so webkit can run on its own thread
        gobject.threads_init()

        # Setup the window properties
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(False)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # the %s will be replaced later on
        html = """
            <html>
                <head>
                    <style>
                        body { background: %s; }
 
                        .button {
                            display: inline-block;
                            padding: 8px;
                            text-align: center;
                            border: 2px solid #729FCF;
                            -webkit-border-radius: 5px;
                            background: #729FCF -webkit-gradient(linear, left top, left bottom,
                                from(rgba(255, 255, 255, 0.45)),
                                to(rgba(255, 255, 255, 0.50)),
                                color-stop(0.4, rgba(255, 255, 255, 0.25)),
                                color-stop(0.6, rgba(255, 255, 255, 0.0)),
                                color-stop(0.9, rgba(255, 255, 255, 0.10)));
 
                            -webkit-user-select: none;
                            cursor: default;
                        }
 
                        .button:hover { border: 2px solid #3E3E3E; }
 
                        .icon { -webkit-user-drag: none; }
                    </style>
                </head>
                <body>
                    <a href="program:/test">
                        <div class="button">
                            <img class="icon" src="http://gwibber.com/icons/22x22/twitter.png" />
                        </div>
                    </a>
                </body>
            </html>
        """
 
        # get the default background color
        bgcolor = self.window.get_style().bg[gtk.STATE_NORMAL]

        # initialize webkit
        self.web = webkit.WebView()

        # tell webkit to load local html and this is where the %s will get
        # replaced
        self.web.load_html_string(html % bgcolor, "file:///")
        # listen for clicks of links
        self.web.connect("navigation-requested", self.on_click_link)
 
        # create a scrollbr and add the webkit item
        scroll = gtk.ScrolledWindow()
        scroll.add(self.web)
 
        # add the scrollbar to the window and show all items on the window
        self.window.add(scroll)
        self.window.show_all()

 
    def on_click_link(self, view, frame, req, data=None):
        """Describes what to do when a href link is clicked"""

        # As Ryan Paul stated he likes to use the prefix program:/ if the
        # link is being used like a button, the else will catch true links
        # and open them in the webbrowser
        uri = req.get_uri()
        if uri.startswith("file:///"):
            return False
        elif uri.startswith("program:/"):
            print uri.split("/")[1]
        else: 
            webbrowser.open(uri)
        return True
  
    def main(self):
        gtk.main()

if __name__ == "__main__":
    button = Button()
    button.main()
