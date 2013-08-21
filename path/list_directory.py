#!/usr/bin/env python

import os

def main():
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

if __name__ == '__main__':
    main()
