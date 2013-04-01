#!/usr/bin/env python
#
# [SNIPPET_NAME: has release target]
# [SNIPPET_CATEGORIES: launchpadlib]
# [SNIPPET_DESCRIPTION: Check if a bug is nominated for a certain release series]
# [SNIPPET_AUTHOR: Markus Korn <thekorn@gmx.de>]
# [SNIPPET_LICENSE: GPL]

# For more Examples see https://help.launchpad.net/API/Examples

from launchpadlib.launchpad import Launchpad, STAGING_SERVICE_ROOT

def has_target(bug, series):
   series_url = str(series)
   for task in bug.bug_tasks:
       if str(task).startswith(series_url):
           return True
   return False

# connect ot the staging service of launchpad
launchpad = Launchpad.login_with("python-snippets", STAGING_SERVICE_ROOT)
# get a bug object
bug = launchpad.bugs[324614]
# get the ubuntu distro object and the jaunty release series
ubuntu = launchpad.distributions["ubuntu"]
jaunty = ubuntu.getSeries(name_or_version="jaunty")
print has_target(bug, jaunty)
