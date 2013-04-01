#!/usr/bin/env python
#
# [SNIPPET_NAME: Delete Records]
# [SNIPPET_CATEGORIES: DesktopCouch]
# [SNIPPET_DESCRIPTION: Delete records from the desktop couch database]
# [SNIPPET_AUTHOR: Andy Breiner <breinera@gmail.com>]
# [SNIPPET_DOCS: http://www.freedesktop.org/wiki/Specifications/desktopcouch/Documentation/SimpleGuide]
# [SNIPPET_LICENSE: GPL]

from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record

#Similar to the fetchrecord.py by Huntly Cameron
#See fetchrecord.py for additional information

db = CouchDatabase("deleterecordsexample", create=True)
record_type = "http://example.com/delete-record-type.html"
record = Record({"first" : "Andy", 
                 "last"  : "Breiner"}, record_type)
db.put_record(record)

record = Record({"first" : "Jono", 
                 "last"  : "Bacon"}, record_type)
db.put_record(record)

results = db.get_records(record_type = record_type, create_view = True)

for records in results:
    record = records.value
    print "First: %s" % record["first"]
    print "Last : %s" % record["last"]
    if record["first"] == "Andy":
      db.delete_record(record["_id"])

