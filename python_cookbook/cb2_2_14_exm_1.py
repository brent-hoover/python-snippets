import RewindableFile
    infile = urllib2.urlopen("http://somewhere/")
    infile = RewindableFile.RewindableFile(infile)
    s = infile.readline()
    if s.startswith("ERROR:"):
          raise Exception(s[:-1])
    infile.seek(0)
    infile.nobuffer()   # Don't buffer the data any more
     ## ... process the XML from infile ...
