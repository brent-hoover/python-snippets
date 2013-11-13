for work_request in iter(queue.get, sentinel):
    process_work_request(work_request)
cleanup_and_terminate()
