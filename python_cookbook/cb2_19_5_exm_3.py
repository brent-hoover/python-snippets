def how_many_unpacked():
    f = inspect.currentframe().f_back.f_back
    bytecode = f.f_code.co_code
    ups_code = opcode.opmap['UNPACK_SEQUENCE']
    if ord(bytecode[f.f_lasti]) == ups_code:
        return ord(bytecode[f.f_lasti+1])
    elif ord(bytecode[f.f_lasti+3]) == ups_code:
        return ord(bytecode[f.f_lasti+4])
    else:
        raise ValueError, "Must be on the RHS of a multiple assignment!"
