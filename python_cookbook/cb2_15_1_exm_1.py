from xmlrpclib import Server
server = Server("http://www.oreillynet.com/meerkat/xml-rpc/server.php")
class MeerkatQuery(object):
    def __init__(self, search, num_items=5, descriptions=0):
        self.search = search
        self.num_items = num_items
	self.descriptions = descriptions
q = MeerkatQuery("[Pp]ython")
print server.meerkat.getItems(q)
