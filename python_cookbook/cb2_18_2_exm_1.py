def uniquer_last(seq, f=None):
    seq = list(seq)
    seq.reverse()
    result = uniquer(seq, f)
    result.reverse()
    return result
