from twisted.application import service, internet
from nevow import rend, loaders, appserver
dct = [{'name':'Mark', 'surname':'White', 'age':'45'},
       {'name':'Valentino', 'surname':'Volonghi', 'age':'21'},
       {'name':'Peter', 'surname':'Parker', 'age':'Unknown'},
      ]
class Pg(rend.Page):
    docFactory = loaders.htmlstr("""
    <html><head><title>Names, Surnames and Ages</title></head>
        <body>
            <ul nevow:data="dct" nevow:render="sequence">
                <li nevow:pattern="item" nevow:render="mapping">
                    <span><nevow:slot name="name"/>&nbsp;</span>
                    <span><nevow:slot name="surname"/>&nbsp;</span>
                    <span><nevow:slot name="age"/></span>
                </li>
            </ul>
        </body>
    </html>
    """)
    def __init__(self, dct):
        self.data_dct = dct
        rend.Page.__init__(self)
site = appserver.NevowSite( Pg(dct) )
application = service.Application("example")
internet.TCPServer(8080, site).setServiceParent(application)
