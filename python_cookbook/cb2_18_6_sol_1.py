class Fifo(list):
    def __init__(self):
        self.back = []
        self.append = self.back.append
    def pop(self):
        if not self:
            self.back.reverse()
            self[:] = self.back
            del self.back[:]
        return super(Fifo, self).pop()
