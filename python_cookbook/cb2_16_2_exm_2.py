if 'foo' in sys.modules:
    foo = sys.modules['foo']
else:
    foofile = open("/path/to/foo.py")      # for some suitable /path/to/...
    foo = importCode(foofile, "foo", 1)
