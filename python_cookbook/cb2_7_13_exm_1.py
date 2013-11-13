class neater(object):
    def __init__(self, row, field_dict):
        self.r = row
        self.d = field_dict
    def __getattr__(self, name):
        try:
            return self.r[self.d[name]]
        except LookupError:
            raise AttributeError
