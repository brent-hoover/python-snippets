import sqlite, cPickle
class Blob(object):
    ''' automatic converter for binary strings '''
    def __init__(self, s): self.s = s
    def _quote(self): return "'%s'" % sqlite.encode(self.s)
# make a test database in memory, get a cursor on it, and make a table
connection = sqlite.connect(':memory:')
cursor = connection.cursor()
cursor.execute("CREATE TABLE justatest (name TEXT, ablob BLOB)")
# Prepare some BLOBs to insert in the table
names = 'aramis', 'athos', 'porthos'
data = {}
for name in names:
    datum = list(name)
    datum.sort()
    data[name] = cPickle.dumps(datum, 2)
# Perform the insertions
sql = 'INSERT INTO justatest VALUES(%s, %s)'
for name in names:
    cursor.execute(sql, (name, Blob(data[name])) )
# Recover the data so you can check back
sql = 'SELECT name, ablob FROM justatest ORDER BY name'
cursor.execute(sql)
for name, blob in cursor.fetchall():
    print name, cPickle.loads(blob), cPickle.loads(data[name])
# Done, close the connection (would be no big deal if you didn't, but...)
connection.close()
