def ilines(source_iterable, eol='\r\n', out_eol='\n'):
    tail = ''
    for block in source_iterable:
        pieces = (tail+block).split(eol)
        tail = pieces.pop()
        for line in pieces:
            yield line + out_eol
    if tail:
        yield tail
if __name__ == '__main__':
    s = 'one\r\ntwo\r,\nthree,four,five\r\n,six,\r\nseven\r\nlast'.split(',')
    for line in ilines(s): print repr(line)
