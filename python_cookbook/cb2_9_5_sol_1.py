import threading, time, Queue
class MultiThread(object):
    def __init__(self, function, argsVector, maxThreads=5, queue_results=False):
        self._function = function
        self._lock = threading.Lock()
        self._nextArgs = iter(argsVector).next
        self._threadPool = [ threading.Thread(target=self._doSome)
                             for i in range(maxThreads) ]
        if queue_results:
            self._queue = Queue.Queue()
        else:
            self._queue = None
    def _doSome(self):
        while True:
            self._lock.acquire()
            try:
                try:
                    args = self._nextArgs()
                except StopIteration:
                    break
            finally:
                self._lock.release()
            result = self._function(args)
            if self._queue is not None:
                self._queue.put((args, result))
    def get(self, *a, **kw):
        if self._queue is not None:
            return self._queue.get(*a, **kw)
        else:
            raise ValueError, 'Not queueing results'
    def start(self):
        for thread in self._threadPool:
            time.sleep(0)    # necessary to give other threads a chance to run
            thread.start()
    def join(self, timeout=None):
        for thread in self._threadPool:
            thread.join(timeout)
if __name__=="__main__":
    import random
    def recite_n_times_table(n):
        for i in range(2, 11):
            print "%d * %d = %d" % (n, i, n * i)
            time.sleep(0.3 + 0.3*random.random())
    mt = MultiThread(recite_n_times_table, range(2, 11))
    mt.start()
    mt.join()
    print "Well done kids!"
