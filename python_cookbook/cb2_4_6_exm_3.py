def flatten(sequence, to_expand=list_or_tuple):
    iterators = [ iter(sequence) ]
    while iterators:
        # loop on the currently most-nested (last) iterator
        for item in iterators[-1]:
            if to_expand(item):
                # subsequence found, go loop on iterator on subsequence
                iterators.append(iter(item))
                break
            else:
                yield item
        else:
            # most-nested iterator exhausted, go back, loop on its parent
            iterators.pop()
