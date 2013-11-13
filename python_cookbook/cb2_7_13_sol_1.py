def fields(cursor):   
    """ Given a DB API 2.0 cursor object that has been executed, returns
    a dictionary that maps each field name to a column index, 0 and up. """
    results = {}
    for column, desc in enumerate(cursor.description):
        results[desc[0]] = column
    return results
