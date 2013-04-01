# [SNIPPET_NAME: Listen to changes in CouchDatabase]
# [SNIPPET_CATEGORIES: DesktopCouch]
# [SNIPPET_DESCRIPTION: Register a callback that will listen to changes in the CouchDatabase]
# [SNIPPET_AUTHOR: Manuel de la Pena <mandel@themacaque.com>]
# [SNIPPET_DOCS: http://www.themacaque.com/wiki/doku.php?id=desktopcouch:listen_to_changes]
# [SNIPPET_LICENSE: GPL]
import time
from desktopcouch.records.server import CouchDatabase

# we are going to be listening to the changes in this callback
def changes_cb(seq=None, id=None, changes=None):
    print seq
    print id
    print changes
 
db = CouchDatabase("listenchangesexample", create=True)

# is better, use glib main loop or twisted task!
while True:
    db.report_changes(changes_cb)
    time.sleep(30)

# got to /home/$USER/.local/share/desktop-couch/couchdb.html and make
# changes to the listenchangesexample to see the callback output
