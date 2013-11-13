class recorder(smart_object):
    count = 0
    events = smart_attr(list)
    def record(self, event):
        self.count += 1
        self.events.append((self.count, event))
