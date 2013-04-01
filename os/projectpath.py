#!/usr/bin/env python
#
# [SNIPPET_NAME: Project Path]
# [SNIPPET_CATEGORIES: os]
# [SNIPPET_DESCRIPTION: The common idiom for setting the root path dynamically from settings.python]
# [SNIPPET_DOCS: ]
# [SNIPPET_AUTHOR: Brent Hoover <brent@hoover.net>]
# [SNIPPET_LICENSE: GPL]

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

