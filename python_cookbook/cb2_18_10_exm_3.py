def primes_oneliner(N):
    aux = {}
    return [aux.setdefault(p, p) for p in range(2, N)
            if 0 not in [p%d for d in aux if p>=d+d]]
