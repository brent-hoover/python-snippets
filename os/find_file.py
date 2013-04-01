#!/usr/bin/env python
#
# [SNIPPET_NAME: Find a file]
# [SNIPPET_CATEGORIES: os]
# [SNIPPET_DESCRIPTION: Recursively search directories for a file]
# [SNIPPET_AUTHOR: Andy Breiner <breinera@gmail.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://docs.python.org/library/os.html, http://diveintopython.org/file_handling/os_module.html]

import os

def look_in_directory(directory):
    """Loop through the current directory for the file, if the current item
       is a directory, it recusively looks through that folder"""

    # Loop over all the items in the directory
    for f in os.listdir(directory):
        # Uncomment the line below to see how the files/folders are searched
        # print "Looking in " + directory

        # If the item is a file check to see if it is what we are looking
        # for, if it is, print that we found it and return true
        if os.path.isfile(os.path.join(directory, f)):
            if f == file_to_find:
                print "Found file: " + os.path.join(directory, f)
                return True

        # If the item is a directory, we recursivley look through that
        # directory if it is found, we again return true
        if os.path.isdir(os.path.join(directory, f)):
            if look_in_directory(os.path.join(directory, f)):
                return True

# we will look for the file recursively
file_to_find = "jono.png"
# Start looking in the home directory (~)
# If it is not found, ie it did not return True, tell the user it was "Not
# Found"
if look_in_directory(os.path.expanduser("~")) != True:
    print "Not Found"
