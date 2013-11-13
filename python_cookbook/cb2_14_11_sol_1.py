#!/usr/bin/python
import sys
import urllib2
import HTMLParser
from xml.dom import minidom, Node
def getElements(node, uri, name):
    ''' recursively yield all elements w/given namespace URI and name '''
    if (node.nodeType==Node.ELEMENT_NODE and
        node.namespaceURI==uri and
        node.localName==name):
        yield node
    for node in node.childNodes:
        for node in getElements(node, uri, name):
            yield node
class LinkGetter(HTMLParser.HTMLParser):
    ''' HTML parser subclass which collecs attributes of link tags '''
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'link':
            self.links.append(attrs)
def getRSS(page):
    ''' given a `page' URL, returns the HREF to the RSS link '''
    contents = urllib2.urlopen(page)
    lg = LinkGetter()
    try:
        lg.feed(contents.read(1000))
    except HTMLParser.HTMLParserError:
        pass
    links = map(dict, lg.links)
    for link in links:
        if (link.get('rel')=='alternate' and
            link.get('type')=='application/rss+xml'):
             return link.get('href')
def getNicks(doc):
    ''' given an XML document's DOM, `doc', yields a triple of info for
        each contact: nickname, blog URL, RSS URL '''
    for element in getElements(doc, 'http://xmlns.com/foaf/0.1/', 'knows'):
        person, = getElements(element, 'http://xmlns.com/foaf/0.1/', 'Person')
        nick, = getElements(person, 'http://xmlns.com/foaf/0.1/', 'nick')
        text, =  nick.childNodes
        nickText = text.toxml()
        blog, = getElements(person, 'http://xmlns.com/foaf/0.1/', 'weblog')
        blogLocation = blog.getAttributeNS(
             'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'resource')
        rss = getRSS(blogLocation)
        if rss:
            yield nickText, blogLocation, rss
def nickToOPMLFragment((nick, blogLocation, rss)):
    ''' given a triple (nickname, blog URL, RSS URL), returns a string
        that's the proper OPML outline tag representing that info '''
    return '''
    <outline text="%(nick)s"
             htmlUrl="%(blogLocation)s"
             type="rss"
             xmlUrl="%(rss)s"/>
    ''' % dict(nick=nick, blogLocation=blogLocation, rss=rss)
def nicksToOPML(fout, nicks):
    ''' writes to file `fout' the OPML document representing the
        iterable of contact information `nicks' '''
    fout.write('''<?xml version="1.0" encoding="utf-8"?>
    <opml version="1.0">
    <head><title>Subscriptions</title></head>
    <body><outline title="Subscriptions">
    ''')
    for nick in nicks:
        print nick
        fout.write(nickToOPMLFragment(nick))
    fout.write("</outline></body></opml>\n")
def docToOPML(fout, doc):
    ''' writes to file `fout' the OPLM for XML DOM `doc' '''
    nicksToOPML(fout, getNicks(doc))
def convertFOAFToOPML(foaf, opml):
    ''' given URL `foaf' to a FOAF page, writes its OPML equivalent to
        a file named by string `opml' '''
    f = urllib2.urlopen(foaf)
    doc = minidom.parse(f)
    docToOPML(file(opml, 'w'), doc)
def getLJUser(user):
    ''' writes an OPLM file `user'.opml for livejournal's FOAF page '''
    convertFOAFToOPML('http://www.livejournal.com/users/%s/data/foaf' % user,
                      user+".opml")
if __name__ == '__main__':
    # example, when this module is run as a main script
    getLJUser('moshez')
