#!/usr/bin/env python
#
# [SNIPPET_NAME: List Directories Content]
# [SNIPPET_CATEGORIES: os]
# [SNIPPET_DESCRIPTION: List the content of the home directory]
# [SNIPPET_AUTHOR: Andy Breiner <breinera@gmail.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://docs.python.org/library/os.html, http://diveintopython.org/file_handling/os_module.html]

import os

# expand ~ to /home/<user_name>
# also print out the content of the home directory as a list
print os.listdir(os.path.expanduser("~"))

# Loop over all the items and determine if they are a file or directory and
# then print them out
directory = os.path.expanduser("~")
for f in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, f)):
        print "File: " + f
    if os.path.isdir(os.path.join(directory, f)):
        print "Directory: " + f
