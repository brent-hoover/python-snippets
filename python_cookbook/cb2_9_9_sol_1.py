from win32event import CreateMutex
from win32api import GetLastError
from winerror import ERROR_ALREADY_EXISTS
from sys import exit
handle = CreateMutex(None, 1, 'A unique mutex name')
if GetLastError() == ERROR_ALREADY_EXISTS:
    # Take appropriate action, as this is the second
    # instance of this script; for example:
    print 'Oh! dear, I exist already.'
    exit(1)
else:
    # This is the only instance of the script; let
    # it do its normal work.  For example:
    from time import sleep
    for i in range(10):
        print "I'm running",i
        sleep(1)
