def bin_with_sign(n):
    if n<0: return '-'+binary(-n)
    else: return binary(n)
