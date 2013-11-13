class SynchronizedObject(GenericWrapper):
    ''' wrap an object and all of its methods with synchronization '''
    def __init__(self, obj, ignore=(), lock=None):
        if lock is None:
            import threading
            lock = threading.RLock()
        GenericWrapper.__init__(self, obj, lock.acquire, lock.release, ignore)
