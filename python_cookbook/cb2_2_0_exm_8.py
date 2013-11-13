from myutils import scanner
def firstword(line):
    print line.split()[0]
file = open('data')
scanner(file, firstword)
