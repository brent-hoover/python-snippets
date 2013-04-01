#!/usr/bin/env python
# [SNIPPET_NAME: Parse an RSS feed]
# [SNIPPET_CATEGORIES: feedparser]  
# [SNIPPET_DESCRIPTION: Parse and iterate over the items in an RSS feed]
# [SNIPPET_AUTHOR: Tim Voet <tim.voet@gmail.com>]
# [SNIPPET_DOCS: http://www.feedparser.org/docs/introduction.html]
# [SNIPPET_LICENSE: GPL]

import feedparser

feed_url = 'http://www.jonobacon.org/feed/'

f = feedparser.parse( feed_url )
print "Feed Title %s" % f.feed.title
for entry in f.entries:
    print "Title: %s" % entry.title
    print "link: %s" % entry.link
    print "Title: %s" % entry.title
        
