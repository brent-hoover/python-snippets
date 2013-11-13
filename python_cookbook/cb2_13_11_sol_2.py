""" Threaded heartbeat server """
import socket, threading, time
UDP_PORT = 43278; CHECK_PERIOD = 20; CHECK_TIMEOUT = 15
class Heartbeats(dict):
    """ Manage shared heartbeats dictionary with thread locking """
    def __init__(self):
        super(Heartbeats, self).__init__()
        self._lock = threading.Lock()
    def __setitem__(self, key, value):
        """ Create or update the dictionary entry for a client """
        self._lock.acquire()
        try:
            super(Heartbeats, self).__setitem__(key, value)
        finally:
            self._lock.release()
    def getSilent(self):
        """ Return a list of clients with heartbeat older than CHECK_TIMEOUT """
        limit = time.time() - CHECK_TIMEOUT
        self._lock.acquire()
        try:
            silent = [ip for (ip, ipTime) in self.items() if ipTime < limit]
        finally:
            self._lock.release()
        return silent
class Receiver(threading.Thread):
    """ Receive UDP packets and log them in the heartbeats dictionary """
    def __init__(self, goOnEvent, heartbeats):
        super(Receiver, self).__init__()
        self.goOnEvent = goOnEvent
        self.heartbeats = heartbeats
        self.recSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recSocket.settimeout(CHECK_TIMEOUT)
        self.recSocket.bind(('', UDP_PORT))
    def run(self):
        while self.goOnEvent.isSet():
            try:
                data, addr = self.recSocket.recvfrom(5)
                if data == 'PyHB':
                    self.heartbeats[addr[0]] = time.time()
            except socket.timeout:
                pass
def main(num_receivers=3):
    receiverEvent = threading.Event()
    receiverEvent.set()
    heartbeats = Heartbeats()
    receivers = []
    for i in range(num_receivers):
        receiver = Receiver(goOnEvent=receiverEvent, heartbeats=heartbeats)
        receiver.start()
        receivers.append(receiver)
    print 'Threaded heartbeat server listening on port %d' % UDP_PORT
    print 'press Ctrl-C to stop'
    try:
        while True:
            silent = heartbeats.getSilent()
            print 'Silent clients: %s' % silent
            time.sleep(CHECK_PERIOD)
    except KeyboardInterrupt:
        print 'Exiting, please wait...'
        receiverEvent.clear()
        for receiver in receivers:
            receiver.join()
        print 'Finished.'
if __name__ == '__main__':
    main()
