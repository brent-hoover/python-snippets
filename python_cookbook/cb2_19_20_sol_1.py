import sys, threading
class SpawnedGenerator(threading.Thread):
    def __init__(self, iterable, queueSize=0):
        threading.Thread.__init__(self)
        self.iterable = iterable
        self.queueSize = queueSize
    def stop(self):
        "Ask iteration to stop as soon as feasible"
        self.stopRequested = True
    def run(self):
        "Thread.start runs this code in another, new thread"
        put = self.queue.put
        try:
            next = iter(self.iterable).next
            while True:
                # report each result, propagate StopIteration
                put((False, next())
                if self.stopRequested:
                    raise StopIteration
        except:
            # report any exception back to main thread and finish
            put((True, sys.exc_info()))
    def execute(self):
        "Yield the results that the other, new thread is obtaining"
        self.queue = Queue.Queue(self.queueSize)
        get = self.queue.get
        self.stopRequested = False
        self.start()              # executes self.run() in other thread
        while True:
            iterationDone, item = get()
            if iterationDone: break
            yield item
        # propagate any exception (unless it's just a StopIteration)
        exc_type, exc_value, traceback = item
        if not isinstance(exc_type, StopIteration):
            raise exc_type, exc_value, traceback
    def __iter__(self):
        "Return an iterator for our executed self"
        return iter(self.execute())
