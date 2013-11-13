for current_value in iterator:
    # if we get here the iterator was not empty, current_value was
    # its first value, and the iterator has been advanced one step
    ## ...use pair (current_value, iterator)...
    # we break at once as we only wanted the first item of iterator
    break
else:
    # if we get here the break did not execute, so the iterator
    # was empty (exhausted)
    ## ...deal with the case of iterator being exhausted...
