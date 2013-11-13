for input_item in stuff_needing_work:
    work_request = make_work_request(input_item)
    queue.put(work_request)
queue.put(sentinel)
