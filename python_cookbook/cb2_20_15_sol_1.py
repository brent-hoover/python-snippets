from opcode import opmap, HAVE_ARGUMENT, EXTENDED_ARG
globals().update(opmap)
def _insert_constant(value, i, code, constants):
    ''' insert LOAD_CONST for value at code[i:i+3].  Reuse an existing
        constant if values coincide, otherwise append new value to the
        list of constants; return index of the value in constants. '''
    for pos, v in enumerate(constants):
        if v is value: break
    else:
        pos = len(constants)
        constants.append(value)
    code[i] = LOAD_CONST
    code[i+1] = pos & 0xFF
    code[i+2] = pos >> 8
    return pos
def _arg_at(i, code):
    ''' return argument number of the opcode at code[i] '''
    return code[i+1] | (code[i+2] << 8)
