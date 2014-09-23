#!/usr/env python

import select
import psycopg2
import psycopg2.extensions

DSN = ''

conn = psycopg2.connect(DSN)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN test;")

print "Waiting for notifications on channel 'test'"
while 1:
    if select.select([conn], [], [], 5) == ([], [], []):
        print "Timeout"
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            print "Got NOTIFY:", notify.pid, notify.channel, notify.payload
