#!/usr/bin/env python
#
# [SNIPPET_NAME: Tee]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Duplicate output to two file descriptors, like Unix tee]
# [SNIPPET_AUTHOR: Akkana Peck <akkana@shallowsky.com>]
# [SNIPPET_DOCS: http://shallowsky.com/blog/programming/python-tee.html]
# [SNIPPET_LICENSE: GPL]
import sys

class tee :
    def __init__(self, _fd1, _fd2) :
        self.fd1 = _fd1
        self.fd2 = _fd2

    def __del__(self) :
        if self.fd1 != sys.stdout and self.fd1 != sys.stderr :
            self.fd1.close()
        if self.fd2 != sys.stdout and self.fd2 != sys.stderr :
            self.fd2.close()

    def write(self, text) :
        self.fd1.write(text)
        self.fd2.write(text)

    def flush(self) :
        self.fd1.flush()
        self.fd2.flush()

if len(sys.argv) <= 1 :
    print "Usage:", sys.argv[0], 'outputfile'
    sys.exit(1)

outputlog = open(sys.argv[1], "w")
stderrsav = sys.stderr
sys.stderr = tee(stderrsav, outputlog)

print >> sys.stderr, "Test 1"
sys.stderr.write("Test 2\n")
