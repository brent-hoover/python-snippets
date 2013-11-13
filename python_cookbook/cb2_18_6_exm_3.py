class FifoDict(dict):
    def __init__(self):
        self.nextin = 0
        self.nextout = 0
    def append(self, data):
        self.nextin += 1
        self[self.nextin] = data
    def pop(self):
        self.nextout += 1
        return dict.pop(self, self.nextout)
