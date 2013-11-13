def bin_fixed(n, bits_per_word=16):
    return bin_twos_complement(n, bits_per_word).rjust(bits_per_word, '0')
