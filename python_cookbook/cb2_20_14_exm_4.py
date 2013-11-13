class recorder(auto_object):
    count = 0
    events = attr(list)
    def record(self, event):
        self.count += 1
        self.events.append((self.count, event))
