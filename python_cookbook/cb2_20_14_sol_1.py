class counter(object):
    def __init__(self):
        self.count = 0
    def increase(self, addend=1):
        self.count += addend
