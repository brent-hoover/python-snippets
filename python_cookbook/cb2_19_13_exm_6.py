for result in unbunch(cursor.fetchmany, 1000):
    doSomethingWith(result)
