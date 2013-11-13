_creating_threads = True
_tss_lock = thread.allocate_lock()
_tss = {}
class TssSequencingError(RuntimeError): pass
def done_creating_threads():
    """ switch from thread-creation to no-more-threads-created state """
    global _creating_threads
    if not _creating_threads:
        raise TssSequencingError('done_creating_threads called twice')
    _creating_threads = False
def get_thread_storage():
    """ Return a thread-specific storage dictionary. """
    thread_id = thread.get_ident()
    # fast approach if thread-creation phase is finished
    if not _creating_threads: return _tss[thread_id]
    # careful approach if we're still creating threads
    try:
        _tss_lock.acquire()
        return _tss.setdefault(thread_id, {})
    finally:
        _tss_lock.release()
