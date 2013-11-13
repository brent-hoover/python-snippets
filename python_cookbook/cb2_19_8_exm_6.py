import itertools
def par_longest_first(padding_item, *sequences):
    iterators = map(iter, sequences)
    for i, it in enumerate(iterators):
        if not i: continue
        iterators[i] = itertools.chain(it, itertools.repeat(padding_item))
    return itertools.izip(iterators)
