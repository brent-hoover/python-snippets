try:
    import threading
except ImportError:
    import dummy_threading as threading
_tss = threading.local()
def get_thread_storage():
    return _tss.__dict__
