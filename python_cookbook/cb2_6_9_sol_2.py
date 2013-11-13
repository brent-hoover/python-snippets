class YourClass(object):
    def __init__(self):
        ## assume there's a lot of work here
    def __copy__(self):
        newcopy = empty_copy(self)
        ## copy some relevant subset of self's attributes to newcopy
        return newcopy
