class Pricing(object):
    def __init__(self, location, event):
        self.location = location
        self.event = event
    def setlocation(self, location):
        self.location = location
    def getprice(self):
        return self.location.getprice()
    def getquantity(self):
        return self.location.getquantity()
    def getdiscount(self):
        return self.event.getdiscount()
    ## and many more such methods
