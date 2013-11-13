log = err = Null()
if verbose:
   log = open('/tmp/log', 'w')
   err = open('/tmp/err', 'w')
log.write('blabla')
err.write('blabla error')
