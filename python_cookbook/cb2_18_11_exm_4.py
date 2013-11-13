def bin_fixed_23(n, bits_per_word=16):
    result = bin_twos_complement(n, bits_per_word)
    return (('0'*bits_per_word)+result)[-bits_per_word:]
