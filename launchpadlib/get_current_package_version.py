#!/usr/bin/env python
#
# [SNIPPET_NAME: get current package version]
# [SNIPPET_CATEGORIES: launchpadlib]
# [SNIPPET_DESCRIPTION: get the latest package version of an ubuntu package]
# [SNIPPET_AUTHOR: Markus Korn <thekorn@gmx.de>]
# [SNIPPET_LICENSE: GPL]

# For more Examples see https://help.launchpad.net/API/Examples

from launchpadlib.launchpad import Launchpad, STAGING_SERVICE_ROOT

# connect ot the staging service of launchpad
launchpad = Launchpad.login_with("python-snippets", STAGING_SERVICE_ROOT)
# get the ubuntu object
ubuntu = launchpad.distributions["ubuntu"]
# look in the main archive and for the current development focus
archive = ubuntu.main_archive
series = ubuntu.current_series
# get a list of all publishec sources of apport in this archive
published_sources = archive.getPublishedSources(exact_match=True,
    source_name="apport", distro_series=series)

# this list is sorted by release date, newest first,
# the first object is the current one
print published_sources[0].source_package_version

