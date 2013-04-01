#!/usr/bin/env python
# [SNIPPET_NAME: Open a tar file]
# [SNIPPET_CATEGORIES: tarfile]
# [SNIPPET_DESCRIPTION: Open's a tar file and list the entries]
# [SNIPPET_AUTHOR: Tim Voet <tim.voet@gmail.com>]
# [SNIPPET_DOCS: http://docs.python.org/library/tarfile.html#module-tarfile]
# [SNIPPET_LICENSE: GPL]

import tarfile
import os
import sys

user =  os.getenv('USERNAME')


filename = '/home/%s/tmp.tgz' % user

print 'about to open %s' % filename
mode = 'r:gz'

if os.path.isfile( filename ) and tarfile.is_tarfile( filename ):
    tf = tarfile.open( filename, mode )
    tf.list()
    tf.close()

