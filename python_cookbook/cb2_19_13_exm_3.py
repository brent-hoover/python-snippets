while True:
    results = cursor.fetchmany(1000)
    if not results: break
    for result in results:
        doSomethingWith(result)
