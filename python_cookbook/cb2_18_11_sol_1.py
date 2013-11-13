def _bytes_to_bits():
    # prepare and return a list of the first 256 int as binary strings
    # start with table of the right length, filled with place-holders
    the_table = 256*[None]
    # we'll repeatedly need to loop on [7, 6, ..., 1, 0], make it once
    bits_per_byte = range(7, -1, -1)
    for n in xrange(256):
        # prepare the nth string: start with a list of 8 place-holders
        bits = 8*[None]
        for i in bits_per_byte:
            # get the i-th bit as a string, shift n right for next bit
            bits[i] = '01'[n&1]
            n >>= 1
        # join up the 8-character string of 0's and 1's into the table
        the_table[n] = ''.join(bits)
    return the_table
# rebind function's name to the table, function not needed any more
_bytes_to_bits = _bytes_to_bits()
