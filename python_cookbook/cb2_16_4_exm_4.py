def report(originalFunction, name, *args, **kw):
    print "%s(%s)"%(name, ', '.join(map(repr, args) +
                                   [k+'='+repr(kw[k]) for k in kw])
    result = originalFunction(*args, **kw)
    if result: print name, '==>', result
    return result
class Sink(object):
    def write(self, text): pass
dest = Sink()
dest.write = curry(report, dest.write, 'write')
print >>dest, 'this', 'is', 1, 'test'
