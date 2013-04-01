"""Tools for creating and displaying histograms."""
import math
from UserDict import IterableUserDict
from tempfile import NamedTemporaryFile

def makelogbuckets(minval, maxval, base=2):
    """Attempt to make logarithmic cutoffs for values between minval
    and maxval."""
    minlog = math.log(max(minval, 1), base)
    maxlog = math.log(maxval, base)

    return [base ** x for x in range(int(minlog), int(maxlog) + 1)]

def guesslogbuckets(minval, maxval, numbuckets=10, startbase=30, step=0.2):
    """Use makelogbuckets() to try to find a base which results in
    roughly the right amount of buckets for logarithmic bucket cutoffs."""
    base = startbase
    while base > 1.01:
        buckets = makelogbuckets(minval, maxval, base)
        if len(buckets) >= numbuckets:
            break
        base -= step
    
    return [int(b) for b in buckets]

def guesslogbucketsfromdata(data, numbuckets=None):
    numbuckets = numbuckets or (math.log10(len(data)) * 10)
    return guesslogbuckets(min(data), max(data), numbuckets)

def uniformbuckets(minval, maxval, numbuckets=10, autoshrink=True):
    """Make numbuckets bucket cutoffs, each of the same size between
    minval and maxval."""
    diff = maxval - minval
    if autoshrink and numbuckets > diff:
        numbuckets = diff
    size = int(math.ceil(diff / float(numbuckets)))
    return range(int(minval), int(maxval) + size, size)

# TODO should use frange here
def uniformbucketsfloat(minval, maxval, numbuckets=10, autoshrink=True):
    """Make numbuckets bucket cutoffs, each of the same size between
    minval and maxval."""
    diff = maxval - minval
    if autoshrink and numbuckets > diff:
        numbuckets = diff
    size = float(diff) / numbuckets
    l = []
    current = minval
    while current < maxval:
        l.append(current)
        current += size
    return l

# uniform sized
def guessuniformbucketsfromdata(data, numbuckets=None, autoshrink=True):
    bucketer = uniformbuckets
    for datum in data:
        if isinstance(datum, float):
            bucketer = uniformbucketsfloat
            break

    numbuckets = numbuckets or (math.log10(len(data)) * 2)
    return bucketer(min(data), max(data), numbuckets, 
                          autoshrink=autoshrink)

# TODO this has some problems
# uniform number of items in buckets
def guessuniformcontentsbucketsfromdata(data, numbuckets=None):
    numitems = len(data)
    numbuckets = numbuckets or (math.log10(numitems) * 2)
    items_per_bucket = numitems / float(numbuckets)

    cur_bucket = []
    cutoffs = []
    for d in sorted(data):
        # print ["%.2f" % (zz * 100) for zz in cutoffs], d, len(cur_bucket)

        if len(cur_bucket) < items_per_bucket or d == cur_bucket[-1]:
            cur_bucket.append(d)
        else:
            cutoffs.append(d)
            # cutoffs.append(cur_bucket[0])
            cur_bucket = [d]

    return cutoffs

def bucket_xy_data_by_x(x, y, bucketfunc, **bucketfuncopts):
    buckets = bucketfunc(x, **bucketfuncopts)
    bucketdict = HistogramBucketDict(buckets)
    for key, val in zip(x, y):
        bucketdict.add(key, amount=val)
    return bucketdict

class HistogramBucketDict(IterableUserDict):
    """Histogram bucket dictionaries have ranges for keys.  They are
    a mapping between { an integer range : count of items added within
    that range }.  In short they're an attempt to "blur" sparse histogram
    data."""
    def __init__(self, cutoffs, data=None):
        """Create a HistogramBucketDict with cutoff points for buckets."""
        IterableUserDict.__init__(self)
        cutoffs = cutoffs[:]
        cutoffs.reverse()
        self.cutoffs = cutoffs
        self.firstcutoff = cutoffs[0]
        self.lastcutoff = cutoffs[-1]
        for cutoff in cutoffs:
            self[cutoff] = 0
        if data:
            self.add_all(data)
    def add(self, key, amount=1):
        """Add 'amount' items for a key.  Whichever bucket 'key' is in
        will have its count incremented by 'amount'."""
        cutoff = self.get_bucket(key)
        self[cutoff] += amount
    def get_bucket(self, key):
        for cutoff in self.cutoffs:
            if key >= cutoff:
                return cutoff
        else: # last bucket
            return self.lastcutoff
        
    def add_all(self, data):
        for item in data:
            self.add(item)
    def bucket_descriptions(self):
        """Get a dictionary descriptions of each bucket.  In the
        description dictionary, keys are the name of the bucket and
        values are tuples for the bucket range: (start, end).  None is
        used to indicate +/- infinity."""
        descs = {self.lastcutoff : (self.lastcutoff, None)}
        for index, cutoff in enumerate(self.cutoffs[:-1]):
            descs[cutoff] = (cutoff, self.cutoffs[index + 1])

        return descs
    def items(self):
        """Returns a list of pairs.  Each pair consists of a bucket
        range and the number of items in that range."""
        descs = self.bucket_descriptions()
        return [(descs[k], v) for k, v in IterableUserDict.items(self)]
    def gnuplot_file(self):
        """Returns a temporary named file which can be used in gnuplot
        to graph this HistogramBucketDict.
        
        Note: Don't close the file returned until you are done with it,
        as it will be deleted."""
        f = NamedTemporaryFile(mode='w')
        items = self.items()
        items.sort()
        for k, v in items:
            f.write("%s %s\n" % (k[0] or 0, v))
        f.flush()
        f.seek(0) # rewind so it will be readily usable

        return f
    def __str__(self):
        """Return an ASCII version of the histogram."""
        items = self.items()
        items.sort()
        ranges = {}
        bars = {}
        maxkeylength = 0
        maxvalue = 0
        for k, v in items:
            if k[1]:
                low = k[1]
                if low == int(low):
                    low = str(int(low))
                else:
                    low = '%.3f' % k[1]
            else:
                low = '-inf'

            if k[0]:
                high = k[0]
                if high == int(high):
                    high = str(int(high))
                else:
                    high = '%.3f' % k[0]
            else:
                high = 'inf'

            ranges[k] = "%s-%s" % (low, high)
            maxkeylength = max(maxkeylength, len(ranges[k]))
            maxvalue = max(maxvalue, v)

        template = "%%%ss: " % maxkeylength
        remaining = 78 - maxkeylength
        for k, v in items:
            bars[v] = '*' * int(math.ceil((v / float(maxvalue)) * remaining))

        s = '\n'.join([(template % ranges[k]) + bars[v]
            for k, v in items])
        return s
    def normalize(self, newmax=1):
        total = 0.0
        for k, v in self.items():
            total += v
        for (start, end), v in list(self.items()):
            self[start] = (v / total) * newmax

def histogramify(amounts, numbuckets=None, normalize=True, 
                 bucket_guesser=guessuniformbucketsfromdata):
    """Fast, one command Histogram creation for the common case."""
    buckets = bucket_guesser(amounts, numbuckets=numbuckets)
    h = HistogramBucketDict(buckets, amounts)
    if normalize:
        h.normalize(100)
    return h

def gnuplot_histograms(histograms, names, scale='uniform', graph_with='boxes'):
    gnuplot_commands = NamedTemporaryFile(mode='w')
    plotfiles = []
    for histogram in histograms:
        plotfiles.append(histogram.gnuplot_file())
    if scale == 'log':
        gnuplot_commands.write('set log y\n')
    gnuplot_commands.write('plot ')
    gnuplot_commands.write(', '.join(["'%s' title '%s' with %s" % \
        (plotfile.name, name, graph_with) 
            for plotfile, name in zip(plotfiles, names)]))
    gnuplot_commands.write('\npause mouse\n')

    gnuplot_commands.flush()
    gnuplot_commands.seek(0)
    import os
    os.system('gnuplot %s' % gnuplot_commands.name)

def test_buckets():
    """Test HistogramBucketDict and gnuplot output."""
    h1 = HistogramBucketDict(guesslogbuckets(0, 500, numbuckets=10))
    for x in range(0, 600):
        h1.add(x)
    h2 = HistogramBucketDict(guesslogbuckets(0, 500, numbuckets=30))
    for x in range(0, 600):
        h2.add(x)
    h3 = HistogramBucketDict(uniformbuckets(0, 500, numbuckets=10))
    for x in range(0, 600):
        h3.add(x)
    h4 = HistogramBucketDict(uniformbuckets(0, 500, numbuckets=30))
    for x in range(0, 600):
        h4.add(x)

    print "==="
    print h1
    print "==="
    print h2
    print "==="
    print h3
    print "==="
    print h4
    print "==="

    gnuplot_histograms([h1, h2, h3, h4], ['log 10', 'log 30', 
                                          'uniform 10', 'uniform 30'])

def autobucket_from_stdin():
    """Main function for simple automatic bucketing and gnuplot visualization.
    Accepts an optional argument (number of buckets), otherwise attempts to
    guess the number of buckets from the size of your data.  stdin should 
    include one value (integer or float) per line."""
    import sys
    try:
        numbuckets = int(sys.argv[-1])
    except:
        numbuckets = None

    values = []
    for line in sys.stdin:
        if line.strip():
            values.append(float(line))
    print "Read", len(values), "values from stdin."
    print "Min:", min(values)
    print "Max:", max(values)

    buckets = guessuniformcontentsbucketsfromdata(values, numbuckets=numbuckets)
    print "Cutoffs:", buckets
    hist = HistogramBucketDict(buckets)
    hist.add_all(values)
    print hist
    gnuplot_histograms([hist], ['Values'])

if __name__ == "__main__":
    autobucket_from_stdin()
