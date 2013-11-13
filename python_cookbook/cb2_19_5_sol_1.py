import inspect, opcode
def how_many_unpacked():
    f = inspect.currentframe().f_back.f_back
    if ord(f.f_code.co_code[f.f_lasti]) == opcode.opmap['UNPACK_SEQUENCE']:
        return ord(f.f_code.co_code[f.f_lasti+1])
    raise ValueError, "Must be a generator on RHS of a multiple assignment!"
def unpack(iterable):
    iterator = iter(iterable)
    for num in xrange(how_many_unpacked()-1):
        yield iterator.next()
    yield iterator
if __name__ == '__main__':
    t5 = range(1, 6)
    a, b, c = unpack(t5)
    print a, b, list(c)
