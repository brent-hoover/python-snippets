if __name__ == '__main__':
    class eg(ChangeCheckerMixin):
        def __init__(self, *a, **k):
            self.L = list(*a, **k)
        def __str__(self):
            return 'eg(%s)' % str(self.L)
        def __getattr__(self, a):
            return getattr(self.L, a)
    x = eg('ciao')
    print 'x =', x, 'is changed =', x.isChanged()
    # emits: x = eg(['c', 'i', 'a', 'o']) is changed = True
    # now, assume x gets saved, then...:
    x.snapshot()
    print 'x =', x, 'is changed =', x.isChanged()
    # emits: x = eg(['c', 'i', 'a', 'o']) is changed = False
    # now we change x...:
    x.append('x')
    print 'x =', x, 'is changed =', x.isChanged()
    # emits: x = eg(['c', 'i', 'a', 'o', 'x']) is changed = True
