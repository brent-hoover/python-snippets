def f_info():
    print "Running function: '%s' Argument: %s"%(sys._getframe(1).f_code.co_name,sys._getframe(1).f_locals)

def check_for_dir(d):
    f_info()
    return os.path.isdir(dir)
