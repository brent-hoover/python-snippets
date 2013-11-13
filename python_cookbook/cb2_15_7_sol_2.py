from twisted.spread import pb
from twisted.internet import reactor
import sys
PORT = 8992
DELAY         = 1
DOG_DELAY     = 2
RESTART_DELAY = 5
class Pinger(object):
    def __init__(self, host):
        self.ping = None
        self.host = host
        self.ball = 0
        self._start()
    def _start(self):
        print 'Waiting for Server', self.host
        dfr = pb.getObjectAt(self.host, PORT, 30)
        dfr.addCallbacks(self._gotRemote, self._remoteFail)
    def _gotRemote(self, remote):
        remote.notifyOnDisconnect(self._remoteFail)
        self.remote = remote
        self._ping()
    def _remoteFail(self, __):
        if self.ping:
            print 'ping failed, canceling and restarting'
            self.ping.cancel()
            self.ping = None
        self.restart = reactor.callLater(RESTART_DELAY, self._start)
    def _watchdog(self):
        print 'ping timed out, canceling and restarting'
        self._start()
    def _ping(self):
        self.dog = reactor.callLater(DOG_DELAY, self._watchdog)
        self.ball += 1
        print 'THROW', self.ball,
        dfr = self.remote.callRemote('Pong', self.ball)
        dfr.addCallbacks(self._pong, self._remoteFail)
    def _pong(self, ball):
        self.dog.cancel()
        print 'CATCH',  ball
        self.ball = ball
        self.ping = reactor.callLater(DELAY, self._ping)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s serverhost' % sys.argv[0]
        sys.exit(1)
    host = sys.argv[1]
    print 'Ping-pong client to host', host
    Pinger(host)
    reactor.run()
