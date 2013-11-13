def cross_loop(*sequences):
    if sequences:
        for x in sequences[0]:
            for y in cross_loop(sequences[1:]):
                yield (x,) + y
    else:
        yield ()
