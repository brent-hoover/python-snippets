#!/usr/bin/env python
#
# [SNIPPET_NAME: Recently used items (async)]
# [SNIPPET_CATEGORIES: Zeitgeist]
# [SNIPPET_DESCRIPTION: Find recently used items from Zeitgeist (asynchronously)]
# [SNIPPET_AUTHOR: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>]
# [SNIPPET_LICENSE: GPL]

# See http://zeitgeist-project.com/documentation for more information

import gobject
from zeitgeist import client, datamodel

try:
    zeitgeist = client.ZeitgeistClient()
except RuntimeError:
    print "Could not connect to Zeitgeist."
    import sys
    sys.exit(1)

mainloop = gobject.MainLoop()

def on_events_received(events):
    events = [datamodel.Event(event) for event in events]
    print "Found the following source code files:"
    for event in events:
        for subject in event.get_subjects():
            print subject.text or subject.uri
    print "-" * 15
    # End the execution of this demo program
    mainloop.quit()

# Fetch the last 10 source code files used
zeitgeist.find_events_for_templates(
    [datamodel.Event.new_for_values(
        subject_interpretation=datamodel.Interpretation.SOURCECODE)],
    on_events_received,
    result_type=datamodel.ResultType.MostRecentSubjects,
    num_events=10)

# Wait for an answer from Zeitgeist
mainloop.run()
