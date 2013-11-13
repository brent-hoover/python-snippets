def list_or_tuple(x):
    return isinstance(x, (list, tuple))
def flatten(sequence, to_expand=list_or_tuple):
    for item in sequence:
        if to_expand(item):
	    for subitem in flatten(item, to_expand):
	        yield subitem
	else:
	    yield item
