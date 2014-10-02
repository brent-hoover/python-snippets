#!/usr/bin/env python
#
# [SNIPPET_NAME: Parse a File]
# [SNIPPET_CATEGORIES: os, Regular Expression]
# [SNIPPET_DESCRIPTION: Recursively go through all the python files and see who has submitted the most (assuming they put their name on them)]
# [SNIPPET_AUTHOR: Andy Breiner <breinera@gmail.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://docs.python.org/library/os.html, # http://docs.python.org/library/re.html]

import os
import re

# A dictionary to store information about who contributed what
# it is assumed that the file has the format
# SNIPPET_AUTHOR: USER_NAME <USER_EMAIL>], if this is not the case then
# this program doesn't count that file
name_list = {}
count_list = {}


def find_python_files(directory):
    """Loop through the current directory and look for a python file, if
       one is found look for the author and create a list showing who has
       contributed the most snippets"""

    # Loop over all the items in the directory
    for f in os.listdir(directory):
        # If the item is a file, check to see if it ends with .py and if
        # so, parse it and find the Author
        if os.path.isfile(os.path.join(directory, f)):
            # this will get the last three characters of the filename
            if f[-3:] == ".py":

                # this will open the file
                file_handler = open(os.path.join(directory, f), "r")

                # this will read all of the file content
                content = file_handler.read()

                # this will close the file
                file_handler.close()

                # we are looking for a string that has "SNIPPET_AUTHOR:"
                # and then any character after it (.) one or more times (+)
                # the newline will end this search
                found = re.search('SNIPPET_AUTHOR:.+', content)
                try:
                    # found.group(0) contains the first and should be only
                    # occurance of this regular expression
                    line = found.group(0)
                    # we do a regular search on the line looking for
                    # the email which should be surrounded by < >
                    email_search = re.search('<.+>', line)

                    # email_search.group(0) has the email, the [1:-1]
                    # tells python to ignore the first character (<)
                    # and the last character (>)
                    email = email_search.group(0)[1:-1]

                    # we look between the : and < which should be the
                    # name
                    name_search = re.search(':.*<', line)

                    # name_search.group(0) has the name, the [1:-1]
                    # tells python to ignore the first character (:)
                    # and the last character (<), finally strip()
                    # removes any extra spaces at the begin or end
                    name = name_search.group(0)[1:-1].strip()

                    # see if this author has already been encountered
                    # before
                    try:
                        count_list[email] = count_list[email] + 1
                    except:
                        # they have not been seen before so add them
                        count_list[email] = 1
                        name_list[email] = name
                except:
                    # something was wrong with finding a regular
                    # expression
                    pass

        # If the item is a directory, we recursivley look through that
        # directory
        if os.path.isdir(os.path.join(directory, f)):
            find_python_files(os.path.join(directory, f))

# go up one level and start searching for python files
location = os.path.join(os.getcwd(), "../")

# Recurse through that location and parse all the python files to see who
# has contributed the most
find_python_files(location)

# sort the collection
count_list = sorted(count_list.items(), key=lambda(key, value): (value, key))

# print the count_list in reverse order while looking inside name_list for
# the given name
count_list.reverse()
for index in range(0, len(count_list)):
    # get the first entry which is similar to (email, count)
    # then get the first item in that entry
    email = count_list[index][0]

    # use the email to lookup the name and then print the name along with
    # the second item in the entry which should be the python snippet count
    print name_list[email] + " " + str(count_list[index][1])
