import base64
print "icon='''\\\n" + base64.encodestring(open("icon.gif").read()) + "'''"
