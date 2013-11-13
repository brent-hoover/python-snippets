for i in range(1, 3):
    print "The loop ran %d time%s" % (i, (lambda:'', lambda:'s')[i!=1]())
