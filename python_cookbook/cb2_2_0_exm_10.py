class MyStream(object):
    def __iter__(self):
        # grab and return text from wherever
        return iter(['a\n', 'b c d\n'])
from myutils import scanner
def firstword(line):
    print line.split()[0]
object = MyStream()
scanner(object, firstword)
