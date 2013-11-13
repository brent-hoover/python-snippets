def attributesFromDict(d):
    self = d.pop('self')
    for n, v in d.iteritems():
        setattr(self, n, v)
