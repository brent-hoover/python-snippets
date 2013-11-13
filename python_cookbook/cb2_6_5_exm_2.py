class AutoDelegator(object):
    delegates = ()
    do_not_delegate = ()
    def __getattr__(self, key):
        if key not in do_not_delegate:
            for d in self.delegates:
                try:
                    return getattr(d, key)
                except AttributeError:
                    pass
        raise AttributeError, key
class Pricing(AutoDelegator):
    def  __init__(self, location, event):
        self.delegates = [location, event]
    def setlocation(self, location):
        self.delegates[0] = location
