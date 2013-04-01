#!/usr/bin/env python
#
# [SNIPPET_NAME: Show notification bubble]
# [SNIPPET_CATEGORIES: Notify OSD]
# [SNIPPET_DESCRIPTION: Show a simple notification bubble]
# [SNIPPET_AUTHOR: Jono Bacon <jono@ubuntu.com>]
# [SNIPPET_LICENSE: GPL]

import pynotify
import os

pynotify.init('someName')

imageURI = 'file://' + os.path.abspath(os.path.curdir) + '/logo.png'

n = pynotify.Notification("message name", "message", imageURI)
n.show()
