def iter_sentinel(a_callable, the_sentinel):
    while True:
        item = a_callable()
        if item == the_sentinel: break
        yield item
