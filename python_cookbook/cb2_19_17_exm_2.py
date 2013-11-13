def is_operator(item):
    return isinstance(item, str)
def operate(x):
    x1, x2 = tee(iter(x))
    while True:
        for item in x1:
            if is_operator(item): break
        else:
	    # we get here when there are no more operators in the input
	    # stream, thus the operate function is entirely done
            return
        if item == '+':
            total = 0
            for item in x2:
                if is_operator(item): break
                total += item
            yield total
        elif item == '*':
            total = 1
            for item in x2:
                if is_operator(item): break
                total *= item
            yield total
