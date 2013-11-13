def logical_lines(physical_lines, joiner=''.join):
    logical_line = []
    for line in physical_lines:
        stripped = line.rstrip()
        if stripped.endswith('\\'):
            # a line which continues w/the next physical line
            logical_line.append(stripped[:-1])
        else:
            # a line which does not continue, end of logical line
            logical_line.append(line)
            yield joiner(logical_line)
            logical_line = []
    if logical_line:
        # end of sequence implies end of last logical line
        yield joiner(logical_line)
if __name__=='__main__':
    text = 'some\\\n', 'lines\\\n', 'get\n', 'joined\\\n', 'up\n'
    for line in text:
        print 'P:', repr(line)
    for line in logical_lines(text, ' '.join):
        print 'L:', repr(line)
