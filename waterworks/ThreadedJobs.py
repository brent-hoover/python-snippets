"""Wraps twisted.python.threadpool in a way that makes more sense to me."""
import time, random
from twisted.python import threadpool, threadable

class ThreadedJobs:
    def __init__(self, func=None, arglistlist=None, workers=5, debug=True):
        """arglistlist is a list of a list of args"""
        self.jobsfinished = 0
        self.jobstodo = 0
        self.debug = debug
        self.tp = threadpool.ThreadPool(workers, workers)
        for arglist in arglistlist or []:
            self.addjob(func, *arglist)

    def start(self):
        self.tp.start()
        while self.jobsfinished < self.getjobstodo():
            time.sleep(0.1)
        self.tp.stop()

    def _run(self, func, *args):
        if self.debug:
            print "Starting", args
        func(*args)
        self.finished(args)

    def finished(self, args):
        if self.debug:
            print "Finished with", args
        self.jobsfinished += 1
    
    def getjobstodo(self):
        return self.jobstodo

    def addjob(self, func, *arglist):
        self.jobstodo += 1
        self.tp.callInThread(self._run, func, *arglist)

    synchronized = ["finished", "getjobstodo", "addjob"]

threadable.synchronize(ThreadedJobs)

if __name__ == "__main__":
    def sleeper(amount, bogusarg):
        print "sleeping for", amount
        time.sleep(amount)
        print "done sleeping for", amount

    times = [(t, 2) for t in range(20)]
    random.shuffle(times)

    tj = ThreadedJobs(sleeper, times)
    tj.start()
