#!/usr/bin/env python
#
# [SNIPPET_NAME: Arguments]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: GNU style arguments]
# [SNIPPET_AUTHOR: Jurjen Stellingwerff <jurjen@stwerff.xs4all.nl>]
# [SNIPPET_LICENSE: GPL]

# example arguments.py

import sys


program = "arguments.py"
version = "0.1"


def indent(size, text):
    """ Indents the lines of a text with 'size' spaces for every newline. """
    i = 0
    res = ""
    for line in text.split("\n"):
        if i > 0:
            res += "\n".ljust(size) + line
        else:
            res += line
        i += 1
    return res


def show_arguments():
    out = []
    size = 0
    for argument in sorted(arguments):
        show = ""
        function, helptext, parameter = arguments[argument]
        if not helptext:
            continue
        if len(argument) > 1:
            show += "    --" + argument
        else:
            show += "-" + argument
        others = False
        for other in sorted(arguments):
            function2, helptext2, parameter2 = arguments[other]
            if function2 == function and other != argument:
                others = True
                if len(other) > 1:
                    show += ", --" + other
                    if parameter2:
                        show += "=" + parameter2
                else:
                    show += ", -" + other
        if parameter and len(argument) > 1:
            show += "=" + parameter
        elif parameter and not others:
            show += " " + parameter
        if len(show) > size and len(show) < 20:
            size = len(show)
        out.append((show, helptext))
    for show, helptext in out:
        if len(show) <= size:
            print ("  %-" + str(size) + "s  %s") % (show, indent(size + 8, helptext))
        else:
            print "  " + show
            print ("   %" + str(size) + "s") % "", indent(size + 8, helptext)


def unknown_argument(argument):
    """ Show an informative error when encountering unknown arguments """
    print program + ": unrecognized option '" + argument + "'"
    print "Try: `" + program + " --help' for more information"
    sys.exit(2)


def parse_arguments():
    """ Reads all the arguments from argv and interprets them in a GNU arguments style """
    i = 0
    paramfunction = None
    for argument in sys.argv:
        i += 1
        if i == 1:
            continue
        if paramfunction:
            paramfunction(argument)
            paramfunction = None
        elif argument.startswith("--"):
            pos = argument.find("=")
            if pos > -1:
                try:
                    function, helptext, parameter = arguments[argument[2:pos]]
                    if not parameter:
                        print "Argument '" + argument[2:pos] + "' cannot have a parameter"
                        sys.exit()
                    function(argument[pos + 1:])
                except KeyError:
                    unknown_argument(argument[:pos])
            else:
                try:
                    function, helptext, parameter = arguments[argument[2:]]
                    function()
                except KeyError:
                    unknown_argument(argument)
        elif argument.startswith("-"):
            for pos in range(1, len(argument)):
                try:
                    function, helptext, parameter = arguments[argument[pos:pos + 1]]
                    if parameter:
                        paramfunction = function
                    else:
                        function()
                except KeyError:
                    unknown_argument(argument[pos:pos + 1])
        else:
            do_rest_arguments(argument)


def add_argument(function, help_text=None, parameter=None):
    """ Add information about an argument:
        - function:  function to call when this argument in given
        - help_text: the help text to show on the help page, omit this parameter on arguments with the same function
        - parameter: this argument needs a parameter
    """
    return function, help_text, parameter


# From here on the actual program code starts

def do_help():
    """ Prints a list of arguments for this program. Normally you would change this function to include more info like examples and another program descriptor. """
    print "Usage: " + program + " [OPTION]... [REST]"
    print "Demonstrates python code for GNU style arguments."
    print ""
    print "Mandatory arguments to long options are mandatory for short options too."
    show_arguments()
    print ""
    print "Report arguments bugs to jurjen@stwerff.xs4all.nl"
    print "Python-snippets homepage: <https://code.launchpad.net/python-snippets>"
    exit()


def do_version():
    """ Show version information of this program """
    print program + " " + version
    print "Copyright (C) 2010 Jurjen Stellingwerff"
    print "Lisense GPL: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>."
    print "This is free software: you are free to change and redistribute it."
    print "There is NO WARRENTY, to the extent permittable by law."
    print ""
    print "Written by Jurjen Stellingwerff."
    exit()


files = []
""" list of files to write to the standard output, can be filled by arguments """

verbose = True


def do_quiet():
    global verbose
    verbose = False


def do_file(filename):
    global files
    files.append(filename)


def do_something(argument):
    print argument


def do_single(argument):
    print argument


def do_rest_arguments(argument):
    print "Rest:", argument


arguments = {
    'version' : add_argument(do_version, 'output version information and exit'),
    'h' : add_argument(do_help, 'display this help and exit'),
    '?' : add_argument(do_help),
    'help' : add_argument(do_help),
    'q' : add_argument(do_quiet, "don't print status messages to stdout"),
    'quiet' : add_argument(do_quiet),
    'f' : add_argument(do_file, 'display this file', parameter='FILE'),
    'file' : add_argument(do_file, parameter='FILE'),
    'this-is-a-bit-too-long-argument' : add_argument(do_something, "when arguments get too long the line splits\nand lines can contain newlines", parameter='SOMETHING'),
    's' : add_argument(do_single, "single token argument with a parameter", parameter='SOMETHING')
}

parse_arguments()
for filename in files:
    if verbose:
        print "Printing file", filename
    try:
        f = open(filename, 'r')
        for line in f.readlines():
            print line.rstrip()
    except IOError:
        print "No such file: '" + filename + "'"


# demonstrate the help page when there are no parameters given
# not very useful in an actual program

if len(sys.argv) == 1:
    do_help()
