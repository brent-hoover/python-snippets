for result in iter(cursor.fetchone, None):
    doSomethingWith(result)
