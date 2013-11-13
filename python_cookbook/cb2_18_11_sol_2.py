def binary(n):
    # check precondition: only non-negative numbers supported
    assert n>=0
    # prepare the list of substrings 8 bits at a time
    bits = []
    while n:
        bits.append(_bytes_to_bit[n&255])
        n >>= 8
    # we need it left-to-right, thus the reverse
    bits.reverse()
    # strip leading '0's, but ensure at least one is left!
    return ''.join(bits).lstrip('0') or '0'
