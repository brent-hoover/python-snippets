#!/usr/bin/env python
# [SNIPPET_NAME: Create a tar file from path]
# [SNIPPET_CATEGORIES: tarfile]
# [SNIPPET_DESCRIPTION: Create a tar file from a path, including compression]
# [SNIPPET_AUTHOR: Tim Voet <tim.voet@gmail.com>]
# [SNIPPET_DOCS: http://docs.python.org/library/tarfile.html#module-tarfile]
# [SNIPPET_LICENSE: GPL]

import tarfile
import os
import sys

user =  os.getenv('USERNAME')

filename = '/home/%s/tmp.tgz' % user
print 'The tar file was created here: %s' % filename
mode = 'w:gz'

file = tarfile.open( filename, mode )

file.add( '/var/log/auth.log' )
file.add( '/var/log/messages' )

file.close()
print 'done'
