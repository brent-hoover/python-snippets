from lxml import html
from random import shuffle

def jumble_words(doc):
    doc = html.fromstring(doc)
    words = doc.text_content().split()
    shuffle(words)
    for el in doc.body.iterdescendants():
        el.text = random_words(el.text, words)
        el.tail = random_words(el.tail, words)
    return html.tostring(doc)

def random_words(text, words):
    if not text:
        return text
    word_count = len(text.split())
    try:
        return ' '.join(words.pop() for i in range(word_count))
    except IndexError:
        # This shouldn't happen, because we should have exactly
        # the right number of words, but just in case...
        return text

from webob import Request

class JumbleMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ)
        req.remove_conditional_headers()
        resp = req.get_response(self.app)
        if resp.content_type == 'text/html':
            resp.body = jumble_words(resp.body)
        return resp(environ, start_response)

import urlparse

class LinkRewriterMiddleware(object):

    def __init__(self, app, dest_href):
        self.app = app
        if dest_href.endswith('/'):
            dest_href = dest_href[:-1]
        self.dest_href = dest_href

    def __call__(self, environ, start_response):
        req = Request(environ)
        dest_path = req.path_info
        dest_href = self.dest_href + dest_path
        req_href = req.application_url
        def link_repl_func(link):
            link = urlparse.urljoin(dest_href, link)
            if not link.startswith(dest_href):
                # Not a local link
                return link
            new_url = req_href + '/' + link[len(dest_href):]
            return new_url
        resp = req.get_response(self.app)
        resp.decode_content()
        if (resp.status_int == 200
            and resp.content_type == 'text/html'):
            doc = html.fromstring(resp.body, base_url=dest_href)
            doc.rewrite_links(link_repl_func)
            resp.body = html.tostring(doc)
        if resp.location:
            resp.location = link_repl_func(resp.location)
        return resp(environ, start_response)



from paste.proxy import Proxy
from wsgiref.validate import validator
import optparse

parser = optparse.OptionParser(usage='%prog PROXY_URL')
parser.add_option(
    '--host',
    metavar='HOST',
    default='localhost',
    help='The host/interface to serve on (default localhost)')
parser.add_option(
    '--port',
    metavar='PORT',
    default='8080',
    help='The port to serve on (default 8080)')
try:
    from weberror.evalexception import EvalException
except ImportError:
    pass
else:
    parser.add_option(
        '--debug',
        action='store_true',
        help='Enable the interactive debugger')

def main():
    options, args = parser.parse_args()
    if not args or len(args) > 1:
        parser.error('You must give one PROXY_URL')
    proxy_url = args[0]
    app = JumbleMiddleware(
        LinkRewriterMiddleware(Proxy(proxy_url), proxy_url))
    if getattr(options, 'debug', False):
        app = EvalException(app)
    app = validator(app)
    from paste.httpserver import serve
    serve(app, host=options.host, port=int(options.port))

if __name__ == '__main__':
    main()

