def fetchsome(cursor, arraysize=1000):
    ''' A generator that simplifies the use of fetchmany '''
    while True:
        results = cursor.fetchmany(arraysize)
        if not results: break
        for result in results:
            yield result
