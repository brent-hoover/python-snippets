the_same_db.put('skidoo', '23')          # add a record
the_same_db.put('words', 'sweet')        # replace a record
for key, data in irecords(the_same_db.cursor()):
    print 'key=%r, data=%r' % (key, data)
# emits (the order may vary):
# key='some', data='0'
# key='example', data='3'
# key='words', data='sweet'
# key='for', data='2'
# key='skidoo', data='23'
