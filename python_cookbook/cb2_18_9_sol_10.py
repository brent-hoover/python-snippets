for i in range(1, 3):
    print "The loop ran %d time%s" % (i, [i==1 and '', i!=1 and 's'][i!=1])
for i in range(1, 3):
    print "The loop ran %d time%s" % (i,
           (i==1 and (lambda:'') or (lambda:'s'))())
