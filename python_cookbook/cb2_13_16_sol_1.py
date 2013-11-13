from twisted.internet import reactor, protocol
from twisted.protocols import irc
class LoggingIRCClient(irc.IRCClient):
    logfile = file('/tmp/msg.txt', 'a+')
    nickname = 'logging_bot'
    def signedOn(self):
        self.join('#test_py')
    def privmsg(self, user, channel, message):
        self.logfile.write(user.split('!')[0] + ' -> ' + message + '\n')
        self.logfile.flush()
def main():
    f = protocol.ReconnectingClientFactory()
    f.protocol = LoggingIRCClient
    reactor.connectTCP('irc.freenode.net', 6667, f)
    reactor.run()
if __name__ == '__main__':
    main()
