import math
def sum_with_partials(arr):
    arr = list(arr)
    size = len(arr)
    iters = int(math.ceil(math.log(size) / math.log(2)))
    step = 1
    for itr in xrange(iters):
        for i in xrange(0, size-step, step+step):
            next_i = i+step
            arr[i] += arr[next_i]
        step += step
    return arr[0]
