from twisted.application import internet, service
from nevow import appserver, compy, inevow, loaders, rend
from nevow import tags as T
# Define some simple classes to be the example's "application data"
class Person(object):
    def __init__(self, firstName, lastName, nickname):
        self.firstName = firstName
        self.lastName = lastName
        self.nickname = nickname
class Bookmark(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
# Adapter subclasses are the right way to join application data to the web:
class PersonView(compy.Adapter):
    """ Render a full view of a Person. """
    __implements__ = inevow.IRenderer
    attrs = 'firstName', 'lastName', 'nickname'
    def rend(self, data):
        return T.div(_class="View person") [
            T.p['Person'],
            T.dl[ [(T.dt[attr], T.dd[getattr(self.original, attr)])
                    for attr in self.attrs]
                ]
            ]
class BookmarkView(compy.Adapter):
    """ Render a full view of a Bookmark. """
    __implements__ = inevow.IRenderer
    attrs = 'name', 'url'
    def rend(self, data):
        return T.div(_class="View bookmark") [
            T.p['Bookmark'],
            T.dl[ [(T.dt[attr], T.dd[getattr(self.original, attr)])
                    for attr in self.attrs]
                ]
            ]
# register the rendering adapters (could be done from a config textfile)
compy.registerAdapter(PersonView, Person, inevow.IRenderer)
compy.registerAdapter(BookmarkView, Bookmark, inevow.IRenderer)
# some example data instances for the 'application'
objs = [
    Person('Valentino', 'Volonghi', 'dialtone'),
    Person('Matt', 'Goodall', 'mg'),
    Bookmark('Nevow', 'http://www.nevow.com'),
    Person('Alex', 'Martelli', 'aleax'),
    Bookmark('Alex', 'http://www.aleax.it/'),
    Bookmark('Twisted', 'http://twistedmatrix.com/'),
    Bookmark('Python', 'http://www.python.org'),
    ]
# a simple Page that renders a list of objects
class Page(rend.Page):
    def render_item(self, ctx, data):
        return inevow.IRenderer(data)
    docFactory = loaders.stan(
        T.html[
            T.body[
                T.ul(data=objs, render=rend.sequence)[
                    T.li(pattern='item')[render_item],
                    ],
                ],
            ]
        )
# start this very-special-purpose tiny toy webserver:
application = service.Application('irenderer')
httpd = internet.TCPServer(8000, appserver.NevowSite(Page()))
httpd.setServiceParent(application)
