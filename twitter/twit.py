# [SNIPPET_NAME: Login and Tweet]
# [SNIPPET_CATEGORIES: twitter, PyGTK]
# [SNIPPET_DESCRIPTION: Log in to your Twitter account and update your status. Uses http://code.google.com/p/python-twitter/]
# [SNIPPET_AUTHOR: Joel Auterson joel.auterson@googlemail.com]
# [SNIPPET_DOCS: http://static.unto.net/python-twitter/0.6/doc/twitter.html]
# [SNIPPET_LICENSE: GPL]

import twitter
import pygtk
import gtk

class GTK_Main():

    def __init__(self):

        def loginClicked(loginButton):

            user = loginUserT.get_text()
            passwd = loginPassT.get_text()
            global api
            api = twitter.Api(username=user, password=passwd)
            login.hide()
            window.show_all()

        def twitClicked(twitButton):

            newtweet = twitE.get_text()
            api.PostUpdate(newtweet)
            gtk.main_quit()

        #Create things - Login

        login = gtk.Window()
        login.connect("destroy", gtk.main_quit)
        login.set_title("Login")
        loginVbox = gtk.VBox(homogeneous=False)
        loginLabel = gtk.Label("Please log in to Twitter!")
        loginHbox1 = gtk.HBox(homogeneous=False, spacing=3)
        loginHbox2 = gtk.HBox(homogeneous=False, spacing=3)
        loginUserL = gtk.Label("User:")
        loginPassL = gtk.Label("Pass:")
        loginUserT = gtk.Entry()
        loginPassT = gtk.Entry()
        loginButton = gtk.Button(label="Log In")
        loginButton.connect("clicked", loginClicked)

        login.add(loginVbox)
        loginVbox.pack_start(loginLabel, expand=False)
        loginVbox.pack_start(loginHbox1, expand=False)
        loginVbox.pack_start(loginHbox2, expand=False)
        loginVbox.pack_start(loginButton, expand=True)
        loginHbox1.pack_start(loginUserL, expand=False)
        loginHbox1.pack_start(loginUserT, expand=True)
        loginHbox2.pack_start(loginPassL, expand=False)
        loginHbox2.pack_start(loginPassT, expand=True)

        #Create tweeting window

        window = gtk.Window()
        window.connect("destroy", gtk.main_quit)
        window.set_title("Twitter")
        twitvbox = gtk.VBox(homogeneous=False)
        twitE = gtk.Entry()
        twitButton = gtk.Button(label="Tweet!")
        window.add(twitvbox)
        twitvbox.pack_start(twitE, expand=False)
        twitvbox.pack_start(twitButton, expand=True)
        twitButton.connect("clicked", twitClicked)

        login.show_all()

GTK_Main()
gtk.main()
