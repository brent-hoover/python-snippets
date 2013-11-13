class Foo(Singleton): pass
class Bar(Foo): pass
f = Foo(); b = Bar()
print f is b, isinstance(f, Foo), isinstance(b, Foo)
# emits False True True
