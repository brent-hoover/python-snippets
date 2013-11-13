def unbunch(next_subseq, *args):
    ''' un-bunch a sequence of subsequences into a linear sequence '''
    while True:
        subseq = next_subseq(*args)
        if not subseq: break
        for item in subseq:
            yield item
