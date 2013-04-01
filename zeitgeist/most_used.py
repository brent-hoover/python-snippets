#!/usr/bin/env python
#
# [SNIPPET_NAME: Recently used items]
# [SNIPPET_CATEGORIES: Zeitgeist]
# [SNIPPET_DESCRIPTION: Find recently used items from Zeitgeist (synchronously)]
# [SNIPPET_AUTHOR: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>]
# [SNIPPET_LICENSE: GPL]

# See http://zeitgeist-project.com/documentation for more information

from zeitgeist import client, datamodel
from datetime import date

try:
    iface = client.ZeitgeistDBusInterface()
except RuntimeError:
    print "Could not connect to Zeitgeist."
    import sys
    sys.exit(1)

min_days_ago = int(raw_input("Up to how many days old may results be? "))
time_range = datamodel.TimeRange.from_seconds_ago(min_days_ago * 3600 * 24)

max_amount_results = int(raw_input("How many results do you want? "))

data_type = raw_input("Which type of items? [All/Video/Music/Image] ")
event_template = datamodel.Event()
if data_type.lower() in ("video", "music", "image"):
    interpretation = getattr(datamodel.Interpretation, data_type.upper())
    event_template.append_subject(
        datamodel.Subject.new_for_values(interpretation=interpretation))

results = iface.FindEvents(
    time_range, # (min_timestamp, max_timestamp) in milliseconds
    [event_template, ],
    datamodel.StorageState.Any,
    max_amount_results,
    datamodel.ResultType.MostRecentSubjects
)

# Pythonize the result
results = (datamodel.Event(result) for result in results)
# Since we are going to loop over the result one by one, we can use parentheses
# to make this a generator, which is more performant.
#
# If we needed to operate on all results at once we would have to use a list
# comprehension instead:
#   results = [datamodel.Event(result) for result in results]

for event in results:
    timestamp = int(event.timestamp) / 1000 # Zeitgeist timestamps are in msec
    print date.fromtimestamp(timestamp).strftime("%d %B %Y")
    for subject in event.get_subjects():
        print " -", subject.text or subject.uri
