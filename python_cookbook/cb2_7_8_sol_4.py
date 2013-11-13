def irecords(curs):
    record = curs.first()
    while record:
        yield record
        record = curs.next()
for key, data in irecords(adb.cursor()):
    print 'key=%r, data=%r' % (key, data)
# emits (the order may vary):
# key='some', data='0'
# key='example', data='3'
# key='words', data='1'
# key='for', data='2'
