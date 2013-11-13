class FifoList(list):
    def pop(self):
        return super(FifoList, self).pop(0)
