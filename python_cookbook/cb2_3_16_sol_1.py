import httplib
import smtplib
# configure script's parameters here
thresholdRate = 1.30
smtpServer = 'smtp.freebie.com'
fromaddr = 'foo@bar.com'
toaddrs = 'your@corp.com'
# end of configuration
url = '/en/financial_markets/csv/exchange_eng.csv'
conn = httplib.HTTPConnection('www.bankofcanada.ca')
conn.request('GET', url)
response = conn.getresponse()
data = response.read()
start = data.index('United States Dollar')
line = data[start:data.index('\n', start)]    # get the relevant line
rate = line.split(',')[-1]                   # last field on the line
if float(rate) < thresholdRate:
   # send email
   msg = 'Subject: Bank of Canada exchange rate alert %s' % rate
   server = smtplib.SMTP(smtpServer)
   server.sendmail(fromaddr, toaddrs, msg)
   server.quit()
conn.close()
