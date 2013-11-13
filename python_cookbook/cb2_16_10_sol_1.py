import inspect
import sys
version_23 = sys.version_info < (2, 4)
def this_list():
    import sys
    d = inspect.currentframe(1).f_locals
    nestlevel = 1
    while '_[%d]' % nestlevel in d: nestlevel += 1
    result = d['_[%d]' % (nestlevel - 1)]
    if version_23: return result.__self__
    else: return result
