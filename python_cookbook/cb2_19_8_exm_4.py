import itertools
def par_loop(padding_item, *sequences):
    iterators = map(iter, sequences)
    num_remaining = len(iterators)
    result = [padding_item] * num_remaining
    while num_remaining:
        for i, it in enumerate(iterators):
            try: 
                 result[i] = it.next()
            except StopIteration:
                 iterators[i] = itertools.repeat(padding_item)
                 num_remaining -= 1
                 result[i] = padding_item
        if num_remaining:
            yield tuple(result)
