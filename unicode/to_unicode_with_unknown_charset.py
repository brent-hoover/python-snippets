#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
from locale import getpreferredencoding


def get_encoding(data):
    for cp in (getpreferredencoding(), 'cp1255', 'cp1250'):
        try:
            _ = unicode(data, cp)
            return cp
        except UnicodeDecodeError:
            pass

    raise Exception('Cannot determine codeset')


def to_unicode(data):
    """ return a version of data where str objects are converted to unicode """

    if isinstance(data, unicode):
        return data
    if isinstance(data, str):
        cp = get_encoding(data)
        return unicode(data, cp)
    elif isinstance(data, collections.Mapping):
        return dict(map(to_unicode, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(to_unicode, data))
    else:
        return data

if __name__ == '__main__':
    unicoded = to_unicode('Joffre Saint-Thiébaut')
    assert(unicoded == u'Joffre Saint-Thiébaut')
    print(unicoded)
