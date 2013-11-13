from twisted.spread import pb
from twisted.internet import reactor
PORT = 8992
class Ponger(pb.Root):
    def remote_Pong(self, ball):
        print 'CATCH', ball,
        ball += 1
        print 'THROW', ball
        return ball
reactor.listenTCP(PORT, pb.BrokerFactory(Ponger()))
reactor.run()
