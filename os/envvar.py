#!/usr/bin/env python
#
# [SNIPPET_NAME: Read an environmental variable]
# [SNIPPET_CATEGORIES: os]
# [SNIPPET_DESCRIPTION: Read and print a given environmental variable]
# [SNIPPET_DOCS: http://docs.python.org/library/os.html]
# [SNIPPET_AUTHOR: Jono Bacon <jono@ubuntu.com>]
# [SNIPPET_LICENSE: GPL]

import os

# display the USERNAME environmental variable
print os.getenv('USERNAME')

