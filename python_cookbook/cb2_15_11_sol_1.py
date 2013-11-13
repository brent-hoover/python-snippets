import httplib
CERT_FILE = '/home/robr/mycert'
PKEY_FILE = '/home/robr/mycert'
HOSTNAME = 'localhost'
conn = httplib.HTTPSConnection(HOSTNAME,
           key_file = PKEY_FILE, cert_file = CERT_FILE)
conn.putrequest('GET', '/ssltest/')
conn.endheaders()
response = conn.getresponse()
print response.read()
