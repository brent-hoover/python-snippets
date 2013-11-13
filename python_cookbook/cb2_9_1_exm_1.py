if __name__ == '__main__':
    import threading
    import time
    class Dummy(object):
        def foo(self):
            print 'hello from foo'
            time.sleep(1)
        def bar(self):
            print 'hello from bar'
        def baaz(self):
            print 'hello from baaz'
    tw = SynchronizedObject(Dummy(), ignore=['baaz'])
    threading.Thread(target=tw.foo).start()
    time.sleep(0.1)
    threading.Thread(target=tw.bar).start()
    time.sleep(0.1)
    threading.Thread(target=tw.baaz).start()
