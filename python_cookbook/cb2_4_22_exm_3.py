data = [ x for line in open(some_file)
           for x in returns(ValueError, float, line) ]
