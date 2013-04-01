# [SNIPPET_NAME: Add record]
# [SNIPPET_CATEGORIES: DesktopCouch]
# [SNIPPET_DESCRIPTION: Add a new record into the database]
# [SNIPPET_AUTHOR: Huntly Cameron <huntly.cameron@gmail.com>]
# [SNIPPET_DOCS: http://www.freedesktop.org/wiki/Specifications/desktopcouch/Documentation/SimpleGuide]
# [SNIPPET_LICENSE: GPL]

from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record

#create the database
db = CouchDatabase("addrecordexample", create=True)

#Records work like python dictionaries, and *should* have an
#online description of how the record should look like.
record_type = "http://example.com/somerecordtype.html"
new_record = Record({"a field" : "a value", 
                     "another field" : "another value"}, record_type)

#put our new record into the datbase
db.put_record(new_record)

#run xdg-open /home/$USER/.local/share/desktop-couch/couchdb.html 
#from the terminal to view the desktopcouch
