#!/usr/bin/env python
#-*- coding: utf-8-*-

# [SNIPPET_NAME: Simple metaclass]
# [SNIPPET_CATEGORIES: Python Core] 
# [SNIPPET_DESCRIPTION: Shows how to create a and use a simple metaclass]
# [SNIPPET_AUTHOR: Florian Diesch <diesch@spamfence.net>]
# [SNIPPET_DOCS: http://www.ibm.com/developerworks/linux/library/l-pymeta.html]
# [SNIPPET_LICENSE: MIT]

# Copyright 2010 Florian Diesch <diesch@spamfence.net>
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

class PropertyMetaclass(type):
    """ 
    This metaclass expects its instances to have a class attribute
    __properties__ that is a dict mapping property names to their
    default values. The metaclass creates the corresponding
    properties
    """

    def __init__(cls, name, bases, dict):
        type.__init__(cls, name, bases, dict)

        props = getattr(cls, '__properties__', {})
        for name, default in props.iteritems():
            type(cls).create_property(cls, name, default)


    def attr_name(cls, prop):
        """ returns the attribute name for property <prop>"""
        return '_%s'%prop

    
    def create_property(cls, name, default):
        """ creates a property named <name> with default value <default>"""
        getter=cls.create_getter(name)
        setter=cls.create_setter(name)
        prop=property(getter, setter, None, None)

        # that's the attribute holding the actual value
        setattr(cls, cls.attr_name(name), default) 
        
        # that's the property
        setattr(cls, name, prop)


    def create_getter(cls, prop):
        """  creates a getter method for property <prop>"""
        attr=cls.attr_name(prop)
        def getter(self):
            print "  class %s: get %s"%(cls.__name__, prop)
            return getattr(self, attr)
        return getter

    def create_setter(cls, prop):
        """  creates a setter method for property <prop>"""
        attr=cls.attr_name(prop)
        def setter(self, value):
            print "  class %s: set %s to '%s'"%(cls.__name__, prop, value)
            setattr(self, attr, value)
        return setter


class Book(object):
    __metaclass__= PropertyMetaclass  # use the metaclass

    __properties__ = {  # some properties
        'author': '[unknown title]',
        'title': '[unknown author]'
        }


if __name__ == '__main__':
    book = Book()
    print '%s by %s'%(book.title, book.author)
    book.author = 'Euclid'
    book.title = 'Elements'
    print '%s by %s'%(book.title, book.author)

    # prints:
    #
    #   class Book: get title
    #   class Book: get author
    # --unknown author-- by --unknown title--
    #   class Book: set author to 'Euclid'
    #   class Book: set title to 'Elements'
    #   class Book: get title
    #   class Book: get author
    # Elements by Euclid





