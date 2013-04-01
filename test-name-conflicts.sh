#!/bin/bash

# find snippets whose filename conflicts with module names in the Python
# Standard Library. This is problematic if a snippet wonts to import a
# standard module and wrongly imports a snippet.

# try to import snippets in python, if an ImportError is raised,
# the filename is OK.
cd $(dirname $0)
files=$(find "." -type f |
        sed 's#.*/##' |
        sed -n 's/^\([a-zA-Z0-9_]*\)\.py$/try:\n import \1\nexcept ImportError:\n pass\nelse:\n print "\1"/p' |
        python)

[ "$files" ] && {
    echo "Files conflicts with module names in the Python Standard Library:"
    echo "$files"
    exit 1
}

