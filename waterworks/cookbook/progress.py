"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/168639
Title: Progress bar class
Submitter: Randy Pargman
Last Updated: 2002/12/11
Version no: 1.0
Category: Files

Description:

Here is a little class that lets you present percent complete information
in the form of a progress bar using the '#' character to represent
completed portions, space to represent incomplete portions, and the
actual percent done (rounded to integer) displayed in the middle:

[############# 33%                               ]

When you initialize the class, you specify the minimum number (usually
0), the maximum number (your file size, for example), and the number of
characters wide you would like the progress bar to be. Note that width
includes the brackets [] on the ends of the progress bar as well.

You'd probably want to use this in conjuction with the curses module,
or something like that so you can over-write the same portion of the
screen to make your updates 'animated'.

Modified by dmcc
    display() and finish() methods
"""
import sys

class ProgressBar:
    def __init__(self, minValue = 0, maxValue = 10, totalWidth=75, 
                 autoreturn=True):
        self.progBar = "[]"   # This holds the progress bar string
        self.min = minValue
        self.max = maxValue
        self.span = maxValue - minValue
        self.width = totalWidth
        self.amount = 0       # When amount == max, we are 100% done 
        self.autoreturn = autoreturn
        self.update_amount(0)  # Build progress bar string
    def update_amount(self, newAmount=0):
        if newAmount < self.min: newAmount = self.min
        if newAmount > self.max: newAmount = self.max
        self.amount = newAmount

        # Figure out the new percent done, round to an integer
        diffFromMin = float(self.amount - self.min)
        try:
            percentDone = (diffFromMin / float(self.span)) * 100.0
        except ZeroDivisionError:
            percentDone = 100
        percentDone = int(percentDone)

        # Figure out how many hash bars the percentage should be
        allFull = self.width - 2
        numHashes = (percentDone / 100.0) * allFull
        numHashes = int(round(numHashes))

        # build a progress bar with hashes and spaces
        self.progBar = "[" + '=' * numHashes + ' ' * (allFull - numHashes) + "]"

        # figure out where to put the percentage, roughly centered
        percentPlace = (len(self.progBar) / 2.0) - len(str(percentDone)) 
        percentPlace = int(percentPlace)
        percentString = " %s%% " % percentDone

        # slice the percentage into the bar
        self.progBar = ''.join((self.progBar[0:percentPlace], 
                                percentString,
                                self.progBar[percentPlace+len(percentString):]))

        if self.autoreturn:
            self.progBar = '\r' + self.progBar
    def __str__(self):
        return str(self.progBar)
    def display(self, stream=sys.stdout):
        stream.write(str(self))
        stream.flush()
    def finish(self, stream=sys.stdout):
        stream.write('\r' + ' ' * self.width + '\r')
        stream.flush()

def autoprogressbar(seq, **progressbar_params):
    """Returns an iterator over seq while displaying a progress bar of
    the appropriate length.  Usage is simple:

    for x in autoprogressbar(some_seq):
        f(x)
    """
    length = len(seq)
    bar = ProgressBar(maxValue=length, **progressbar_params)
    for i, item in enumerate(seq):
        bar.update_amount(i)
        if i < length:
            bar.display()
        else:
            bar.finish()
        yield item

    bar.finish()

if __name__ == "__main__":
    import time, sys
    prog = ProgressBar(0, 100, 34, autoreturn=False)
    prog2 = ProgressBar(0, 100, 34)
    for i in xrange(1001):
        prog.update_amount(i / 10.0)
        prog2.update_amount(100 - (i / 5.0))
        sys.stdout.write("\r%s" % prog)
        sys.stdout.write("%s" % prog2)
        sys.stdout.flush()
        time.sleep(.01)
