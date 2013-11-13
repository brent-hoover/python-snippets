def binary_slow(n):
    assert n>=0
    bits = []
    while n:
        bits.append('01'[n&1])
        n >>= 1
    bits.reverse()
    return ''.join(bits) or '0'
