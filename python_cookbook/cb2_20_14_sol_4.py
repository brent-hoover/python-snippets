class recorder(object):
    count = 0
    events = auto_attr('events', list)
    def record(self, event):
        self.count += 1
        self.events.append((self.count, event))
