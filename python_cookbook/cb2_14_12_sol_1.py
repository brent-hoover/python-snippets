#!/usr/bin/python
from twisted.internet import reactor, protocol, defer
from twisted.web import client
import feedparser, time, sys, cStringIO
from out import rss_feed as rss_feeds
DEFERRED_GROUPS = 60       # Number of simultaneous connections
INTER_QUERY_TIME = 300     # Max Age (in seconds) of each feed in the cache
TIMEOUT = 30               # Timeout in seconds for the web request
# dict cache's structure will be the following: { 'URL': (TIMESTAMP, value) }
cache = {}
class FeederProtocol(object):
    def __init__(self):
        self.parsed = 0
        self.error_list = []
    def isCached(self, site):
        ''' do we have site's feed cached (from not too long ago)? '''
        # how long since we last cached it (if never cached, since Jan 1 1970)
        elapsed_time = time.time() - cache.get(site, (0, 0))[0]
        return elapsed_time < INTER_QUERY_TIME
    def gotError(self, traceback, extra_args):
        ''' an error has occurred, print traceback info then go on '''
        print traceback, extra_args
        self.error_list.append(extra_args)
    def getPageFromMemory(self, data, addr):
        ''' callback for a cached page: ignore data, get feed from cache '''
        return defer.succeed(cache[addr][1])
    def parseFeed(self, feed):
        ''' wrap feedparser.parse to parse a string '''
        try: feed+''
        except TypeError: feed = str(feed)
        return feedparser.parse(cStringIO.StringIO(feed))
    def memoize(self, feed, addr):
        ''' cache result from feedparser.parse, and pass it on '''
        cache[addr] = time.time(), feed
        return feed
    def workOnPage(self, parsed_feed, addr):
        ''' just provide some logged feedback on a channel feed '''
        chan = parsed_feed.get('channel', None)
        if chan:
            print chan.get('title', '(no channel title?)')
        return parsed_feed
    def stopWorking(self, data=None):
        ''' just for testing: we close after parsing a number of feeds.
            Override depending on protocol/interface you use to communicate
            with this RSS aggregator server.
        '''
        print "Closing connection number %d..." % self.parsed
        print "=-"*20
        self.parsed += 1
        print 'Parsed', self.parsed, 'of', self.END_VALUE
        if self.parsed >= self.END_VALUE:
            print "Closing all..."
            if self.error_list:
                print 'Observed', len(self.error_list), 'errors'
                for i in self.error_list:
                    print i
            reactor.stop()
    def getPage(self, data, args):
        return client.getPage(args, timeout=TIMEOUT)
    def printStatus(self, data=None):
        print "Starting feed group..."
    def start(self, data=None, standalone=True):
        d = defer.succeed(self.printStatus())
        for feed in data:
            if self.isCached(feed):
                d.addCallback(self.getPageFromMemory, feed)
                d.addErrback(self.gotError, (feed, 'getting from memory'))
            else:
                # not cached, go and get it from the web directly
                d.addCallback(self.getPage, feed)
                d.addErrback(self.gotError, (feed, 'getting'))
                # once gotten, parse the feed and diagnose possible errors
                d.addCallback(self.parseFeed)
                d.addErrback(self.gotError, (feed, 'parsing'))
                # put the parsed structure in the cache and pass it on
                d.addCallback(self.memoize, feed)
                d.addErrback(self.gotError, (feed, 'memoizing'))
            # now one way or another we have the parsed structure, to
            # use or display in whatever way is most appropriate
            d.addCallback(self.workOnPage, feed)
            d.addErrback(self.gotError, (feed, 'working on page'))
            # for testing purposes only, stop working on each feed at once
            if standalone:
                d.addCallback(self.stopWorking)
                d.addErrback(self.gotError, (feed, 'while stopping'))
        if not standalone:
            return d
class FeederFactory(protocol.ClientFactory):
    protocol = FeederProtocol()
    def __init__(self, standalone=False):
        self.feeds = self.getFeeds()
        self.standalone = standalone
        self.protocol.factory = self
        self.protocol.END_VALUE = len(self.feeds) # this is just for testing
        if standalone:
            self.start(self.feeds)
    def start(self, addresses):
        # Divide into groups all the feeds to download
        if len(addresses) > DEFERRED_GROUPS:
            url_groups = [[] for x in xrange(DEFERRED_GROUPS)]
            for i, addr in enumerate(addresses):
                url_groups[i%DEFERRED_GROUPS].append(addr[0])
        else:
            url_groups = [[addr[0]] for addr in addresses]
        for group in url_groups:
            if not self.standalone:
                return self.protocol.start(group, self.standalone)
            else:
                self.protocol.start(group, self.standalone)
    def getFeeds(self, where=None):
        # used for a complete refresh of the feeds, or for testing purposes
        if where is None:
            return rss_feeds
        return None
if __name__=="__main__":
    f = FeederFactory(standalone=True)
    reactor.run()
