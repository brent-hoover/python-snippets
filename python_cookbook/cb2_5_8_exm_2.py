import heapq
def top10(data):
    return heapq.nsmallest(10, data)
