def pp(cursor, data=None, check_row_lengths=False):
    if not data:
        data = cursor.fetchall()
    names = []
    lengths = []
    rules = []
    for col, field_description in enumerate(cursor.description):
        field_name = field_description[0]
        names.append(field_name)
        field_length = field_description[2] or 12
        field_length = max(field_length, len(field_name))
        if check_row_lengths:
            # double-check field length, if it's unreliable
            data_length = max([ len(str(row[col])) for row in data ])
            field_length = max(field_length, data_length)
        lengths.append(field_length)
        rules.append('-' * field_length)
    format = " ".join(["%%-%ss" % l for l in lengths])
    result = [ format % tuple(names), format % tuple(rules) ]
    for row in data:
        result.append(format % tuple(row))
    return "\n".join(result)
