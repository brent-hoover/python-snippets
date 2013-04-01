#!/usr/bin/env python
#
# [SNIPPET_NAME: Upstart service status]
# [SNIPPET_CATEGORIES: dbus, Upstart]
# [SNIPPET_DESCRIPTION: Shows how to obtain the status and pids of a service from Upstart, using D-Bus]
# [SNIPPET_AUTHOR: Scott James Remnant <scott@ubuntu.com>]
# [SNIPPET_LICENSE: MIT]
# [SNIPPET_DOCS: http://upstart.ubuntu.com/wiki/DBusInterface]

import dbus

bus = dbus.SystemBus()

# Get the manager object
upstart = bus.get_object("com.ubuntu.Upstart", "/com/ubuntu/Upstart")

# Lookup the object for the job we're interested in
# this represents the configuration file on the disk
path = upstart.GetJobByName("udev", dbus_interface="com.ubuntu.Upstart0_6")
job = bus.get_object("com.ubuntu.Upstart", path)

# Now lookup the running instance
# and get its properties
path = job.GetInstance([], dbus_interface="com.ubuntu.Upstart0_6.Job")
instance = bus.get_object("com.ubuntu.Upstart", path)
props = instance.GetAll("com.ubuntu.Upstart0_6.Instance", dbus_interface=dbus.PROPERTIES_IFACE)

# Print out the goal (start or stop), state (running, etc.) and the list of
# pids
print "%s/%s" % (props["goal"], props["state"])
for process, pid in props["processes"]:
	print "\t%s %s" % (process, pid)
