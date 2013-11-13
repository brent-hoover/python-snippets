def has_bal_par(s):
    op = 0
    for c in s:
        if c=='(':
            op += 1
        elif c==')':
            if op == 0:
                return False
            op -= 1
    return op == 0
