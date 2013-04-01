#!/usr/bin/env python
#
# [SNIPPET_NAME: Regex String Stip]
# [SNIPPET_CATEGORIES: string]
# [SNIPPET_DESCRIPTION: Strip characters from a string using regex in one line]
# [SNIPPET_DOCS:  None]
# [SNIPPET_AUTHOR: Brent Hoover <brent@hoover.net>]
# [SNIPPET_LICENSE: GPL]
import re


def strip_chars_for_url(self, string_to_clean):
    return ''.join(re.findall(r'[A-Za-z0-9\-\._]', string_to_clean.replace(' ', '-')))

