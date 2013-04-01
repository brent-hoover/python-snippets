#!/usr/bin/env python
#
# [SNIPPET_NAME: Send a message]
# [SNIPPET_CATEGORIES: Gwibber]
# [SNIPPET_DESCRIPTION: Send a message using the Gwibber API]
# [SNIPPET_AUTHOR: Jono Bacon <jono@ubuntu.com>]
# [SNIPPET_LICENSE: GPL]

import gwibber.lib

# first create the message - remember to keep it under 140 chars
message = "Sending a message from a python-snippets example! - see https://wiki.ubuntu.com/PythonSnippets for details!"

# create a connection to the running Gwibber service
gw = gwibber.lib.GwibberPublic()

# send the message
gw.SendMessage(message)

# now check your microblogging service(s) to see the message there! :-)
