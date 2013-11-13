import threading
class TestThread(threading.Thread):
    def __init__(self, name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        """ main control loop """
        print "%s starts" % (self.getName(),)
        count = 0
        while not self._stopevent.isSet():
            count += 1
            print "loop %d" % (count,)
            self._stopevent.wait(self._sleepperiod)
        print "%s ends" % (self.getName(),)
    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)
if __name__ == "__main__":
    testthread = TestThread()
    testthread.start()
    import time
    time.sleep(5.0)
    testthread.join()
