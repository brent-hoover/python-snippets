class MyClass(object):
    class_attr = 23
    @CachedClassAttribute
    def square(cls):
        return cls.class_attr * cls.class_attr
x = MyClass()
y = MyClass()
print x.square
# emits: 529
print y.square
# emits: 529
del MyClass.square
print x.square         # raises an AttributeError exception
