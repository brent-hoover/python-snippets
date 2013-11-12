#!/usr/bin/env python
#
# [SNIPPET_NAME: Generate modified list]
# [SNIPPET_CATEGORIES: core]
# [SNIPPET_DESCRIPTION: How to generate a modified list by iterating over each element of another list]
# [SNIPPET_AUTHOR: Scott Ferguson <scottwferg@gmail.com>]
# [SNIPPET_LICENSE: GPL]

first_list = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [x + 1 for x in first_list] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print result
