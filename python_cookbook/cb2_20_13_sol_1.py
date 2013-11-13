# a couple of classes that you write:
class super1(object):
    def __new__(cls, *args, **kwargs):
        obj = super(super1, cls).__new__(cls, *args, **kwargs)
        obj.attr1 = []
        return obj
    def __str__(self):
        show_attr = []
        for attr, value in sorted(self.__dict__.iteritems()):
            show_attr.append('%s:%r' % (attr, value))
        return '%s with %s' % (self.__class__.__name__,
                               ', '.join(show_attr))
class super2(object):
    def __new__(cls, *args, **kwargs):
        obj = super(super2, cls).__new__(cls, *args, **kwargs)
        obj.attr2 = {}
        return obj
# typical beginners' code, inheriting your classes but forgetting to
# call its superclasses' __init__ methods
class derived(super1, super2):
    def __init__(self):
        self.attr1.append(111)
        self.attr3 = ()
# despite the typical beginner's error, you won't get support calls:
d = derived()
print d
# emits: derived with attr1:[111], attr2:{}, attr3:()
