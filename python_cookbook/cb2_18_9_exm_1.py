class cond(object):
    def __getitem__(self, sl):
        if sl.start: return sl.stop
        else: return sl.step
cond = cond()
