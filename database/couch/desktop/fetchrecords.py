# [SNIPPET_NAME: Fetch Records]
# [SNIPPET_CATEGORIES: DesktopCouch]
# [SNIPPET_DESCRIPTION: Fetch records from the desktop couch database]
# [SNIPPET_AUTHOR: Huntly Cameron <huntly.cameron@gmail.com>]
# [SNIPPET_DOCS: http://www.freedesktop.org/wiki/Specifications/desktopcouch/Documentation/SimpleGuide]
# [SNIPPET_LICENSE: GPL]

from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record

#First, we want to put a record into a database and then get it out
#create the database
db = CouchDatabase("fetchrecordsexample", create=True)

#Create some records
record_type = "http://example.com/fetch-record-type.html"
new_record = Record({"afield" : "a value", 
                     "anotherfield" : "another value"}, record_type)
another_record = Record({"afield" : "some value", 
                         "anotherfield" : "some other value"}, record_type)

#put our new records into the datbase
db.put_record(new_record)
db.put_record(another_record)

#Fetch all the records in the database and display them
results = db.get_records(record_type = record_type, create_view = True)

for records in results:
    record = records.value
    print "a field: %s" % record["afield"]
    print "another field: %s" % record["anotherfield"]



