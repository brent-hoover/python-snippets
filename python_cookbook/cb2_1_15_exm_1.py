def expand_at_linestart(P, tablen=8):
    import re
    def exp(mo):
        return mo.group().expand(tablen)
    return ''.join([ re.sub(r'^\s+', exp, s) for s in P.splitlines(True) ])
