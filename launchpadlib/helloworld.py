#!/usr/bin/env python
#
# [SNIPPET_NAME: launchpadlib Hello-World]
# [SNIPPET_CATEGORIES: launchpadlib]
# [SNIPPET_DESCRIPTION: Get launchpad username via launchpadlib]
# [SNIPPET_AUTHOR: Markus Korn <thekorn@gmx.de>]
# [SNIPPET_LICENSE: GPL]

# For more Examples see https://help.launchpad.net/API/Examples

from launchpadlib.launchpad import Launchpad, STAGING_SERVICE_ROOT

# connect to the staging service of launchpad
launchpad = Launchpad.login_with("python-snippets", STAGING_SERVICE_ROOT)
# print username
print 'Hello, %s!' % launchpad.me.display_name
