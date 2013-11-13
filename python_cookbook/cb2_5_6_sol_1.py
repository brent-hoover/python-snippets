def process_all_in_random_order(data, process):
    # first, put the whole list into random order
    random.shuffle(data)
    # next, just walk over the list linearly
    for elem in data: process(elem)
