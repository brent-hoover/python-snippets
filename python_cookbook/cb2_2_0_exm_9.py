from cStringIO import StringIO
from myutils import scanner
def firstword(line): print line.split()[0]
string = StringIO('one\ntwo xxx\nthree\n')
scanner(string, firstword)
