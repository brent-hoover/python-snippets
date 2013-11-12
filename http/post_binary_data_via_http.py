req = urllib2.Request("http://example.com", data, {'Content-Type': 'application/octet-stream'})
urllib2.urlopen(req)
