def operate_with_auxiliary_list(x):
    aux = []
    for item in x:
	if is_operator(item):
	    if item == '+':
		yield sum(aux)
	    elif item == '*':
		total = 1
		for item in aux:
		    total *= item
		yield total
	    aux = []
	else:
	    aux.append(item)
