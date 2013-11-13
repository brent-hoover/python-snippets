class hist(dict):
    ## ...
    def counts(self, reverse=False):
        return _sorted_keys(self, self, reverse)
class hist1(list):
    ## ...
    def counts(self, reverse=False):
        return _sorted_keys(self, xrange(len(self)), reverse)
