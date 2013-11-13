while True:
    work_request = queue.get()
    if work_request == sentinel:
        break
    process_work_request(work_request)
cleanup_and_terminate()
