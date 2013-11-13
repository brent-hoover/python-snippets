def logical_lines(physical_lines, joiner=''.join, separator=''):
    return joiner(physical_lines).replace('\\\n', separator).splitlines(True)
