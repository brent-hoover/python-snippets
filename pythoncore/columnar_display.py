#!/usr/bin/env python
#
# [SNIPPET_NAME: Columnar display]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Print a list of arguments in several columns]
# [SNIPPET_AUTHOR: Akkana Peck <akkana@shallowsky.com>]
# [SNIPPET_LICENSE: GPL]
def columnar_display(list, pagewidth=77) :
    maxlen = 0
    for item in list :
        l = len(str(item))
        if l > maxlen :
            maxlen = l
    maxlen += 2   # space it out a little more
    numcol = int(pagewidth / maxlen)

    i = 0
    for item in list :
        print '{0:{1}}'.format(item, maxlen),
        i += 1
        if i % numcol == 0 :
            print '\n',

list = [ 'Python Core', 'Python VTE', 'Regular Expression', 'socket',
         'tarfile', 'Testing', 'threading', 'twitter', 'unittest',
         'Upstart', 'Webkit', 'Zeitgeist' ]

columnar_display(list)
