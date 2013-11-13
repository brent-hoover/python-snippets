import xml.parsers.expat
def parsefile(file):
    parser = xml.parsers.expat.ParserCreate()
    parser.ParseFile(open(file, "r"))
