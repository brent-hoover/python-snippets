import time
from twisted.application import internet, service
from twisted.internet import protocol
from twisted.python import log
UDP_PORT = 43278; CHECK_PERIOD = 20; CHECK_TIMEOUT = 15
class Receiver(protocol.DatagramProtocol):
    """ Receive UDP packets and log them in the clients dictionary """
    def datagramReceived(self, data, (ip, port)):
        if data == 'PyHB':
            self.callback(ip)
class DetectorService(internet.TimerService):
    """ Detect clients not sending heartbeats for too long """
    def __init__(self):
        internet.TimerService.__init__(self, CHECK_PERIOD, self.detect)
        self.beats = {}
    def update(self, ip):
        self.beats[ip] = time.time()
    def detect(self):
        """ Log a list of clients with heartbeat older than CHECK_TIMEOUT """
        limit = time.time() - CHECK_TIMEOUT
        silent = [ip for (ip, ipTime) in self.beats.items() if ipTime < limit]
        log.msg('Silent clients: %s' % silent)
application = service.Application('Heartbeat')
# define and link the silent clients' detector service
detectorSvc = DetectorService()
detectorSvc.setServiceParent(application)
# create an instance of the Receiver protocol, and give it the callback
receiver = Receiver()
receiver.callback = detectorSvc.update
# define and link the UDP server service, passing the receiver in
udpServer = internet.UDPServer(UDP_PORT, receiver)
udpServer.setServiceParent(application)
# each service is started automatically by Twisted at launch time
log.msg('Asynchronous heartbeat server listening on port %d\n'
    'press Ctrl-C to stop\n' % UDP_PORT)
