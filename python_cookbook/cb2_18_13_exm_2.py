if v < 0:
## ...
elif v < 0.5:
    n, d = farey((v-v+1)/v, lim)     # lim is wrong; decide what you want
    return d, n
elif v > 1:
    intpart = floor(v)
    n, d = farey(v-intpart)
    return n+intpart*d, d
## ...
