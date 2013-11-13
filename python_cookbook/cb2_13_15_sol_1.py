import md5, sys
from twisted.internet import protocol, reactor
from twisted.protocols import basic
from twisted.python import usage
def hashPassword(password, salt):
    ''' compute and return MD5 hash for given password and `salt'. '''
    p1 = md5.md5(password).hexdigest() + '.' + salt.strip()
    return md5.md5(p1).hexdigest()
class DIPProtocol(basic.LineReceiver):
    """ Implementation of GnuDIP protocol(TCP) as described at:
    http://gnudip2.sourceforge.net/gnudip-www/latest/gnudip/html/protocol.html
    """
    delimiter = '\n'
    def connectionMade(self):
        ''' at connection, we start in state "expecting salt". '''
        basic.LineReceiver.connectionMade(self)
        self.expectingSalt = True
    def lineReceived(self, line):
        ''' we received a full line, either "salt" or normal response '''
        if self.expectingSalt:
            self.saltReceived(line)
            self.expectingSalt = False
        else:
            self.responseReceived(line)
    def saltReceived(self, salt):
        """ Override this 'abstract method' """
        raise NotImplementedError
    def responseReceived(self, response):
        """ Override this 'abstract method' """
        raise NotImplementedError
class DIPUpdater(DIPProtocol):
    """ A simple class to update an IP, then disconnect. """
    def saltReceived(self, salt):
        ''' having received `salt', login to the DIP server '''
        password = self.factory.getPassword()
        username = self.factory.getUsername()
        domain = self.factory.getDomain()
        msg = '%s:%s:%s:2' % (username, hashPassword(password, salt), domain)
        self.sendLine(msg)
    def responseReceived(self, response):
        ''' response received: show errors if any, then disconnect. '''
        code = response.split(':', 1)[0]
        if code == '0':
            pass  # OK
        elif code == '1':
            print 'Authentication failed'
        else:
            print 'Unexpected response from server:', repr(response)
        self.transport.loseConnection()
class DIPClientFactory(protocol.ClientFactory):
     """ Factory used to instantiate DIP protocol instances with
         correct username, password and domain.
     """
     protocol = DIPUpdater
     # simply collect data for login and provide accessors to them
     def __init__(self, username, password, domain):
         self.u = username
         self.p = password
         self.d = domain
     def getUsername(self):
         return self.u
     def getPassword(self):
         return self.p
     def getDomain(self):
         return self.d
     def clientConnectionLost(self, connector, reason):
         ''' terminate script when we have disconnected '''
         reactor.stop()
     def clientConnectionFailed(self, connector, reason):
         ''' show error message in case of network problems '''
         print 'Connection failed. Reason:', reason
class Options(usage.Options):
     ''' parse options from commandline or config script '''
     optParameters = [['server', 's', 'gnudip2.yi.org', 'DIP Server'],
                      ['port', 'p', 3495, 'DIP Server  port'],
                      ['username', 'u', 'durdn', 'Username'],
                      ['password', 'w', None, 'Password'],
                      ['domain', 'd', 'durdn.yi.org', 'Domain']]
if __name__ == '__main__':
     # running as main script: first, get all the needed options
     config = Options()
     try:
         config.parseOptions()
     except usage.UsageError, errortext:
         print '%s: %s' % (sys.argv[0], errortext)
         print '%s: Try --help for usage details.' % (sys.argv[0])
         sys.exit(1)
     server = config['server']
     port = int(config['port'])
     password = config['password']
     if not password:
         print 'Password not entered. Try --help for usage details.'
         sys.exit(1)
     # and now, start operations (via Twisted's ``reactor'')
     reactor.connectTCP(server, port,
            DIPClientFactory(config['username'], password, config['domain']))
     reactor.run()
