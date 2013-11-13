def munge2(alist):
    if type(alist) is list:       # a very bad idea
        munge1(alist)
    else: raise TypeError, "expected list, got %s" % type(alist)
