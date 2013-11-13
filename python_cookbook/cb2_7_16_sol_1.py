class Param(object):
    ''' a class to wrap any single parameter '''
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'Param(%r)' % (self.value,)
def to_qmark(chunks):
    ''' prepare SQL query in '?' style '''
    query_parts = []
    params = []
    for chunk in chunks:
        if isinstance(chunk, Param):
            params.append(chunk.value)
            query_parts.append('?')
        else:
            query_parts.append(chunk)
    return ''.join(query_parts), params
def to_numeric(chunks):
    ''' prepare SQL query in ':1' style '''
    query_parts = []
    params = []
    for chunk in chunks:
        if isinstance(chunk, Param):
            params.append(chunk.value)
            query_parts.append(':%d' % len(params))
        else:
            query_parts.append(chunk)
    # DCOracle2 needs, specifically, a _tuple_ of parameters:
    return ''.join(query_parts), tuple(params)
def to_named(chunks):
    ''' prepare SQL query in ':name' style '''
    query_parts = []
    params = {}
    for chunk in chunks:
        if isinstance(chunk, Param):
            name = 'p%d' % len(params)
            params[name] = chunk.value
            query_parts.append(':%s' % name)
        else:
            query_parts.append(chunk)
    return ''.join(query_parts), params
def to_format(chunks):
    ''' prepare SQL query in '%s' style '''
    query_parts = []
    params = []
    for chunk in chunks:
        if isinstance(chunk, Param):
            params.append(chunk.value)
            query_parts.append('%s')
        else:
            query_parts.append(chunk.replace('%', '%%'))
    return ''.join(query_parts), params
def to_pyformat(chunks):
    ''' prepare SQL query in '%(name)s' style '''
    query_parts = []
    params = {}
    for chunk in chunks:
        if isinstance(chunk, Param):
            name = 'p%d' % len(params)
            params[name] = chunk.value
            query_parts.append('%%(%s)s' % name)
        else:
            query_parts.append(chunk.replace('%', '%%'))
    return ''.join(query_parts), params
converter = {}
for paramstyle in ('qmark', 'numeric', 'named', 'format', 'pyformat'):
    converter[paramstyle] = globals['to_' + param_style]
def execute(cursor, converter, chunked_query):
    query, params = converter(chunked_query)
    return cursor.execute(query, params)
if __name__=='__main__':
    query = ('SELECT * FROM test WHERE field1>', Param(10),
             ' AND field2 LIKE ', Param('%value%'))
    print 'Query:', query
    for paramstyle in ('qmark', 'numeric', 'named', 'format', 'pyformat'):
        print '%s: %r' % (paramstyle, converter[param_style](query))
