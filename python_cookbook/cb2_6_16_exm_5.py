class Borg(object):
    _shared_state = {}
    def __new__(cls, *a, **k):
        obj = object.__new__(cls, *a, **k)
        obj.__dict__ = cls._shared_state
        return obj
    def __hash__(self): return 9      # any arbitrary constant integer
    def __eq__(self, other):
        try: return self.__dict__ is other.__dict__
        except AttributeError: return False
