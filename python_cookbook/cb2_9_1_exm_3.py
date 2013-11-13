self.lock.acquire()
try:
   ## The "real" application code for the method
finally:
    self.lock.release()
