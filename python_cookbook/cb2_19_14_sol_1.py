import heapq
def merge(*subsequences):
    # prepare a priority queue whose items are pairs of the form
    # (current-value, iterator), one each per (non-empty) subsequence
    heap = []
    for subseq in subsequences:
        iterator = iter(subseq)
	for current_value in iterator:
	    # subseq is not empty, therefore add this subseq's pair
	    # (current-value, iterator) to the list
	    heap.append((current_value, iterator))
	    break
    # make the priority queue into a heap
    heapq.heapify(heap)
    while heap:
	# get and yield lowest current value (and corresponding iterator)
        current_value, iterator = heap[0]
        yield current_value
	for current_value in iterator:
	    # subseq is not finished, therefore add this subseq's pair
	    # (current-value, iterator) back into the priority queue
	    heapq.heapreplace(heap, (current_value, iterator))
	    break
	else:
	    # subseq has been exhausted, therefore remove it from the queue
            heapq.heappop(heap)
