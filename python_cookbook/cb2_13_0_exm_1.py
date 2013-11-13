import sys, urllib
def reporthook(*a): print a
for url in sys.argv[1:]:
    i = url.rfind('/')
    file = url[i+1:]
    print url, "->", file
    urllib.urlretrieve(url, file, reporthook)
