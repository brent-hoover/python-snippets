probability = 0.333
n, d = farey(probability, 100)
print "Odds are %d : %d" % (n, d-n)
# emits: Odds are 1 : 2
