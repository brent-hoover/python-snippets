import codecs, sys
sys.stdout = codecs.lookup('iso8859-1')[-1](sys.stdout)
