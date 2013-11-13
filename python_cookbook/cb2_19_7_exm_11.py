import itertools as IT
def windowed(iterable, pre=1, post=1, padding=None):
    # tee-off one iterator for each index in the window
    copies = IT.tee(iterable, pre + 1 + post)
    pre_copies, copy, post_copies = copies[:pre], copies[pre], copies[pre+1:]
    # iterators before the element have their start filled in with the
    # padding value.  no need to slice off the ends, izip will do that.
    pre_copies = [IT.chain(IT.repeat(padding, pre - i), itr)
                  for i, itr in enumerate(pre_copies)]
    # iterators after the element have their starts sliced off and their
    # end filled in with the padding value, endlessly repeated.
    post_copies = [IT.chain(IT.islice(itr, i + 1, None), IT.repeat(padding))
                   for i, itr in enumerate(post_copies)]
    # zip the elements with their preceding and following elements
    return IT.izip(*(pre_copies + [copy] + post_copies))
