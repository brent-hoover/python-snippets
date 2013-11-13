def primes_less_than(N):
    # make `primes' a list of known primes < N
    primes = [x for x in (2, 3, 5, 7, 11, 13) if x < N]
    if N <= 17: return primes
    # candidate primes are all odd numbers less than N and over 15,
    # not divisible by the first few known primes, in descending order
    candidates = [x for x in xrange((N-2)|1, 15, -2)
                  if x % 3 and x % 5 and x % 7 and x % 11 and x % 13]
    # make `top' the biggest number that we must check for compositeness
    top = int(N ** 0.5)
    while (top+1)*(top+1) <= N:
        top += 1
    # main loop, weeding out non-primes among the remaining candidates
    while True:
        # get the smallest candidate: it must be a prime
        p = candidates.pop()
        primes.append(p)
        if p > top:
            break
        # remove all candidates which are divisible by the newfound prime
        candidates = filter(p.__rmod__, candidates)
    # all remaining candidates are prime, add them (in ascending order)
    candidates.reverse()
    primes.extend(candidates)
    return primes
