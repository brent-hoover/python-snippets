_tss = {}
try:
    import thread
except ImportError:
    # We're running on a single-threaded platform (or, at least, the Python
    # interpreter has not been compiled to support threads), so we just return
    # the same dict for every call -- there's only one thread around anyway!
    def get_thread_storage():
        return _tss
else:
    # We do have threads; so, to work:
    _tss_lock = thread.allocate_lock()
    def get_thread_storage():
        """ Return a thread-specific storage dictionary. """
        thread_id = thread.get_ident()
        _tss_lock.acquire()
        try:
            return _tss.set_default(thread_id, {})
        finally:
            _tss_lock.release()
