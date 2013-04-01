#!/usr/bin/env python
#
# [SNIPPET_NAME: Reversing strings]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: How to reverse the contents of a string]
# [SNIPPET_AUTHOR: Scott Ferguson <scottwferg@gmail.com>]
# [SNIPPET_LICENSE: GPL]

text = ['Hello', 'world', 'Go hang a salami I\'m a lasagna hog']

for word in text:
    print word[::-1]
