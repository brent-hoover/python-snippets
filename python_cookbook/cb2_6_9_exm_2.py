class YourClass(object):
    ## ...
    def __deepcopy__(self, memo):
        newcopy = empty_copy(self)
        # use copy.deepcopy(self.x, memo) to get deep copies of elements
        # in the relevant subset of self's attributes, to set in newcopy
        return newcopy
