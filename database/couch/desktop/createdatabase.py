# [SNIPPET_NAME: Create a Database]
# [SNIPPET_CATEGORIES: DesktopCouch] 
# [SNIPPET_DESCRIPTION: Creating a new database in desktopcouch]
# [SNIPPET_AUTHOR: Huntly Cameron <huntly.cameron@gmail.com>]
# [SNIPPET_DOCS: http://www.freedesktop.org/wiki/Specifications/desktopcouch/Documentation/SimpleGuide]
# [SNIPPET_LICENSE: GPL]

from desktopcouch.records.server import CouchDatabase

#Create a database object. Your database needs to exist. 
#If it doesn't, you can create it by passing create=True.
db = CouchDatabase('createdatabaseexample', create=True)

#run xdg-open /home/$USER/.local/share/desktop-couch/couchdb.html 
#from the terminal to view the desktopcouch
