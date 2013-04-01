# [SNIPPET_NAME: Add an attachment to a Desktopcouch Record]
# [SNIPPET_CATEGORIES: DesktopCouch]
# [SNIPPET_DESCRIPTION: Shows how to add an attachment to a Desktopcouch Record that will be stored and replicated by CouchDB]
# [SNIPPET_AUTHOR: Manuel de la Pena <mandel@themacaque.com>]
# [SNIPPET_DOCS: http://www.themacaque.com/wiki/doku.php?id=desktopcouch:create_attachments]
# [SNIPPET_LICENSE: GPL]
import sys
from desktopcouch.records.record import Record
from desktopcouch.records.server import CouchDatabase

# get the jpg to add from the command line

if len(sys.argv) > 1:
    path = sys.argv[0]
    db = CouchDatabase("addattachment", create=True)
    record = Record(record_type="url")
    record.attach(path, "blob", "image/jpg")
    db.put_record(record)
else:
    print "Please pass the path of the jpg to add."

# got to /home/$USER/.local/share/desktop-couch/couchdb.html to see the 
# attached file
