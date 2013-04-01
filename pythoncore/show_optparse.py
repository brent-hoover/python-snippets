#!/usr/bin/env python
#
# [SNIPPET_NAME: Show optparse]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: GNU style arguments via optparse]
# [SNIPPET_AUTHOR: Jurjen Stellingwerff <jurjen@stwerff.xs4all.nl>]
# [SNIPPET_LICENSE: GPL]

# example show_optparse.py

import optparse, sys

program = "show_optparse.py"
# usefull when the program alters from the normal python file

version = """%prog 0.1
Copyright (C) 2010 Jurjen Stellingwerff
Lisense GPL: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRENTY, to the extent permittable by law.

Written by Jurjen Stellingwerff.
"""

usage = "Usage: %prog [OPTION]... [REST]"
description = "Demonstrates python code for GNU style arguments."

def do_single(option, opt, value, parser):
    print value

parser = optparse.OptionParser(usage=usage, version=version, description=description, prog=program)
parser.add_option("-?", action="help", help=optparse.SUPPRESS_HELP)
parser.add_option("-f", "--file", dest="filename", action="append",
                  help="display this file", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_option("--this-is-a-bit-too-long-argument", metavar="SOMETHING",
                  help="when arguments get too long the line splits, this also works for the longer help strings")
parser.add_option("-s", metavar="SOMETHING", action="callback", callback=do_single, type="string",
                  help="single token argument with a parameter")
group = optparse.OptionGroup(parser, "\nReport arguments bugs to jurjen@stwerff.xs4all.nl\nPython-snippets homepage: <https://code.launchpad.net/python-snippets>")
parser.add_option_group(group)

(options, args) = parser.parse_args()

if options.this_is_a_bit_too_long_argument:
    print options.this_is_a_bit_too_long_argument

if options.filename:
    for filename in options.filename:
        if options.verbose:
            print "Printing file",filename
        try:
            f = open(filename)
            for line in f.readlines():
                print line.rstrip()
        except IOError:
            print "No such file: "+options.filename

for rest in args:
    print "Rest:",rest

# demonstrate the help page when there are no parameters given
# not very useful in an actual program

if len(sys.argv)==1:
    parser.print_help()

