import win32con, win32api, os
# create a file, just to show how to manipulate it
thefile = 'test'
f = open('test', 'w')
f.close()
# to make the file hidden...:
win32api.SetFileAttributes(thefile, win32con.FILE_ATTRIBUTE_HIDDEN)
# to make the file readonly:
win32api.SetFileAttributes(thefile, win32con.FILE_ATTRIBUTE_READONLY)
# to be able to delete the file we need to set it back to normal:
win32api.SetFileAttributes(thefile, win32con.FILE_ATTRIBUTE_NORMAL)
# and finally we remove the file we just made
os.remove(thefile)
