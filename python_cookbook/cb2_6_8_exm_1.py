class Lower(object):
    def __init__(self, s=''):
        self.s = s
    def _getS(self):
        return self._s
    def _setS(self, s):
        self._s = s.lower()
    s = property(_getS, _setS)
