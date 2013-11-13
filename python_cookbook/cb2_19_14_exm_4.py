try:
    current_value = iterator.next()
    # if we get here the iterator was not empty, current_value was
    # its first value, and the iterator has been advanced one step
    ## ...use pair (current_value, iterator)...
except StopIteration:
    # if we get here the iterator was empty (exhausted)
    ## ...deal with the case of iterator being exhausted...
