class TraceNormal(object):
    ' state for normal level of verbosity '
    def startMessage(self):
        self.nstr = self.characters = 0
    def emitString(self, s):
        self.nstr += 1
        self.characters += len(s)
    def endMessage(self):
        print '%d characters in %d strings' % (self.characters, self.nstr)
class TraceChatty(object):
    ' state for high level of verbosity '
    def startMessage(self):
        self.msg = []
    def emitString(self, s):
        self.msg.append(repr(s))
    def endMessage(self):
        print 'Message: ', ', '.join(self.msg)
class TraceQuiet(object):
    ' state for zero level of verbosity '
    def startMessage(self): pass
    def emitString(self, s): pass
    def endMessage(self): pass
class Tracer(object):
    def __init__(self, state): self.state = state
    def setState(self, state): self.state = state
    def emitStrings(self, strings):
        self.state.startMessage()
        for s in strings: self.state.emitString(s)
        self.state.endMessage()
if __name__ == '__main__':
    t = Tracer(TraceNormal())
    t.emitStrings('some example strings here'.split())
# emits: 21 characters in 4 strings
    t.setState(TraceQuiet())
    t.emitStrings('some example strings here'.split())
# emits nothing
    t.setState(TraceChatty())
    t.emitStrings('some example strings here'.split())
# emits: Message: 'some', 'example', 'strings', 'here'
