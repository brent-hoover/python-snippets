#!/usr/bin/env python
#
# [SNIPPET_NAME: Lookup website]
# [SNIPPET_CATEGORIES: GIO]
# [SNIPPET_DESCRIPTION: Lookup a website and make a connection]
# [SNIPPET_AUTHOR: Andrew Breiner <breinera@gmail.com>]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_DOCS: http://www.pygtk.org/docs/pygobject/gio-class-reference.html]

# This example was taken from an example done in the Vala programming
# language.

import gio

# Setup a resolver and lookup the ip address for www.google.com
resolver = gio.resolver_get_default()
addresses = resolver.lookup_by_name("www.google.com")

# Print the ip addresses that are associated with www.google.com
print "www.google.com resolves to :"
for i in range(0, len(addresses)):
    print addresses[i].to_string()

# Connect to www.google.com
client = gio.SocketClient()
socket = gio.InetSocketAddress(addresses[0], 80)
conn = client.connect(socket, gio.Cancellable())

# Send a message to www.google.com
message = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n";
stream = conn.get_output_stream()
stream.write (message, gio.Cancellable())

# Recieve a message from www.google.com which is
# HTTP/1.1 200 OK
istream = gio.DataInputStream (conn.get_input_stream())
message = istream.read_line()
print "received status line: " + message
