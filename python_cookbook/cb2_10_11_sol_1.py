import winsound
try:
    winsound.PlaySound("*", winsound.SND_ALIAS)
except RuntimeError, e:
    print 'Sound system has problems,', e
else:
    print 'Sound system is OK'
