import random
prec = 5
data = [F(random.random()*10-5) for i in xrange(1000)]
print '%s\t%s\t%s' %('Computed', 'ULP Error', 'Method')
print '%s\t%s\t%s' %('--------', '---------', '------')
for f in avgsum, avgrun, avgrun_kahan:
    result = f(data)
    print '%s\t%6d\t\t%s' % (result, result.error(), f.__name__)
print '\n%r\tbaseline average using full precision' % result.full
