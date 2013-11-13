if __name__ == '__main__':               # usual guard for example usage
    class Foo(object):
        def __init__(self, x=23, y=42):
            self.x, self.y = x, y
    f = Foo()
    print f
    # emits: &lt;__main__.Foo object at 0x38f770&gt;
    set_rich_str(f)
    print f
    # emits:
    # x               23
    # y               42
    set_rich_str(f, on=False)
    print f
    # emits: &lt;__main__.Foo object at 0x38f770&gt;
