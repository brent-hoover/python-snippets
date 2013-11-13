try: Person.address = ''
except AttributeError, err: print 'raised %r as expected' % err
try: me.address = ''
except AttributeError, err: print 'raised %r as expected' % err
