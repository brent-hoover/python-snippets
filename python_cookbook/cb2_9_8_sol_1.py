import signal
# credit: original idea was based on an article by David Mertz
# http://gnosis.cx/publish/programming/charming_python_b7.txt
# some example 'microthread' generators
def empty(name):
    """ This is an empty task for demonstration purposes. """
    while True:
        print "<empty process>", name
        yield None
def terminating(name, maxn):
    """ This is a counting task for demonstration purposes. """
    for i in xrange(maxn):
        print "Here %s, %s out of %s" % (name, i, maxn)
        yield None
    print "Done with %s, bailing out after %s times" % (name, maxn)
def delay(duration=0.8):
    """ Do nothing at all for 'duration' seconds. """
    import time
    while True:
        print "<sleep %d>" % duration
        time.sleep(duration)
        yield None
class GenericScheduler(object):
    def __init__(self, threads, stop_asap=False):
        signal.signal(signal.SIGINT, self.shutdownHandler)
        self.shutdownRequest = False
        self.threads = threads
        self.stop_asap = stop_asap
    def shutdownHandler(self, n, frame):
        """ Initiate a request to shutdown cleanly on SIGINT."""
        print "Request to shut down."
        self.shutdownRequest = True
    def schedule(self):
        def noop():
            while True: yield None
        n = len(self.threads)
        while True:
            for i, thread in enumerate(self.threads):
                try: thread.next()
                except StopIteration:
                    if self.stop_asap: return
                    n -= 1
                    if n==0: return
                    self.threads[i] = noop()
                if self.shutdownRequest:
                    return
if __name__== "__main__":
    s = GenericScheduler([ empty('boo'), delay(), empty('foo'),
                           terminating('fie', 5), delay(0.5),
                        ], stop_asap=True)
    s.schedule()
    s = GenericScheduler([ empty('boo'), delay(), empty('foo'),
                           terminating('fie', 5), delay(0.5),
                        ], stop_asap=False)
    s.schedule()
