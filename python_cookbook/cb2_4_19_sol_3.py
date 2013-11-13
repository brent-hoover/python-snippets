class DataHolder(object):
    def __init__(self, value=None):
        self.value = value
    def set(self, value):
        self.value = value
        return value
    def get(self):
        return self.value
# optional and strongly discouraged, but nevertheless handy at times:
import __builtin__
__builtin__.DataHolder = DataHolder
__builtin__.data = data = DataHolder()
