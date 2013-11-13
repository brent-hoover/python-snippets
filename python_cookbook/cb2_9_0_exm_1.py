somelock.acquire()
try:
    ## operations needing the lock (keep to a minimum!)
finally:
    somelock.release()
