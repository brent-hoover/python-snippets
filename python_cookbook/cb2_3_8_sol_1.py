import time
def is_dst():
    return bool(time.localtime().tm_isdst)
