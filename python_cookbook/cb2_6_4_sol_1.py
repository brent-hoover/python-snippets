class Chainmap(object):
    def __init__(self, *mappings):
        # record the sequence of mappings into which we must look
        self._mappings = mappings
    def __getitem__(self, key):
        # try looking up into each mapping in sequence
        for mapping in self._mappings:
            try:
                return mapping[key]
            except KeyError:
                pass
        # `key' not found in any mapping, so raise KeyError exception
        raise KeyError, key
    def get(self, key, default=None):
        # return self[key] if present, otherwise `default'
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        # return True if `key' is present in self, otherwise False
        try:
            self[key]
            return True
        except KeyError:
            return False
