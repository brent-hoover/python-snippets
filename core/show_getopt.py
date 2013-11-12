#!/usr/bin/env python
#
# [SNIPPET_NAME: Show getopt]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: GNU style arguments via getopt]
# [SNIPPET_AUTHOR: Jurjen Stellingwerff <jurjen@stwerff.xs4all.nl>]
# [SNIPPET_LICENSE: GPL]
import getopt, sys

program = "getopt"
version = "0.1"

def do_version():
    """ Show version information of this program """
    print program+" "+version
    print """Copyright (C) 2010 Jurjen Stellingwerff
Lisense GPL: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRENTY, to the extent permittable by law.

Written by Jurjen Stellingwerff."""
    exit()

def do_help():
    """ Prints a list of arguments for this program. Normally you would change this function to include more info like examples and another program descriptor. """
    print "Usage: "+program+" [OPTION]... [REST]"
    print """Demonstrates python code for GNU style arguments.
Mandatory arguments to long options are mandatory for short options too.
  -f, --file=FILE  display this file
  -h, -?, --help   display this help and exit
  -q, --quiet      don't print status messages to stdout
      --this-is-a-bit-too-long-argument=SOMETHING
                   when arguments get too long the line splits
                      and lines can contain newlines
      --version    output version information and exit

Report arguments bugs to jurjen@stwerff.xs4all.nl
Python-snippets homepage: <https://code.launchpad.net/python-snippets>"""
    exit()

def main():
    files = []
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "?qhf:", ["help", "file=", "version", "this-is-a-bit-too-long-argument="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    output = None
    verbose = True
    for option, argument in opts:
        if option in ("-f", "--file"):
            files.append(argument)
        elif option in ("-h", "-?", "--help"):
            do_help()
        elif option in ("--version"):
            do_version()
        elif option in ("-q", "--quiet"):
            verbose = False
        elif option in ("--this-is-a-bit-too-long-argument"):
            print argument
        else:
            assert False, "unhandled option"

    for filename in files:
        if verbose:
            print "Printing file",filename
        try:
            f = open(filename, 'r')
            for line in f.readlines():
                print line.rstrip()
        except IOError:
            print "No such file: '"+filename+"'"

    for text in args:
        print "Rest:",text

    # demonstrate the help page when there are no parameters given
    # not very useful in an actual program

    if len(sys.argv)==1:
        do_help()

if __name__ == "__main__":
    main()

