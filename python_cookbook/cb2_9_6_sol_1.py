import candygram as cg
class ExampleThread(object):
    """A thread-class with just a single counter value and a stop flag."""
    def __init__(self):
        """ Initialize the counter to 0, the running-flag to True. """
        self.val = 0
        self.running = True
    def increment(self):
        """ Increment the counter by one. """
        self.val += 1
    def sendVal(self, msg):
        """ Send current value of counter to requesting thread. """
        req = msg[0]
        req.send((cg.self(), self.val))
    def setStop(self):
        """ Set the running-flag to False. """
        self.running = False
    def run(self):
        """ The entry point of the thread. """
        # Register the handler functions for various messages:
        r = cg.Receiver()
        r.addHandler('increment', self.increment)
        r.addHandler((cg.Process, 'value'), self.sendVal, cg.Message)
        r.addHandler('stop', self.setStop)
        # Keep handling new messages until a stop has been requested
        while self.running:
            r.receive()
