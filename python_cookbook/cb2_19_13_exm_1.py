cursor.execute('select * from HUGE_TABLE')
for result in cursor.fetchall():
    doSomethingWith(result)
