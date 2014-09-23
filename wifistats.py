import time
from pythonwifi.iwlibs import Wireless
 
wifi = Wireless(''eth1'')
 
while True:
    print wifi.getStatistics()[1].getSignallevel()
    time.sleep(1)
