def q(x):
    if len(x)>1:
	lt = [i for i in x if cmp(i,x[0]) == -1 ]
	eq = [i for i in x if cmp(i,x[0]) == 0 ]
	gt = [i for i in x if cmp(i,x[0]) == 1 ]
	return q(lt) + eq + q(gt)
    else:
	return x
