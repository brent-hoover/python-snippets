def bin_twos_complement(n, bits_per_word=16):
    if n<0: n = (2<<bits_per_word) + n
    return binary(n)
