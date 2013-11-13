import MySQLdb, cPickle
# Connect to a DB, e.g., the test DB on your localhost, and get a cursor
connection = MySQLdb.connect(db="test")
cursor = connection.cursor()
# Make a new table for experimentation
cursor.execute("CREATE TABLE justatest (name TEXT, ablob BLOB)")
try:
    # Prepare some BLOBs to insert in the table
    names = 'aramis', 'athos', 'porthos'
    data = {}
    for name in names:
        datum = list(name)
        datum.sort()
        data[name] = cPickle.dumps(datum, 2)
    # Perform the insertions
    sql = "INSERT INTO justatest VALUES(%s, %s)"
    for name in names:
        cursor.execute(sql, (name, MySQLdb.escape_string(data[name])) )
    # Recover the data so you can check back
    sql = "SELECT name, ablob FROM justatest ORDER BY name"
    cursor.execute(sql)
    for name, blob in cursor.fetchall():
        print name, cPickle.loads(blob), cPickle.loads(data[name])
finally:
    # Done. Remove the table and close the connection.
    cursor.execute("DROP TABLE justatest")
    connection.close()
