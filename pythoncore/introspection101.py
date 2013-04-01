#!/usr/bin/env python
#-*- encoding: utf8 -*-
#
# [SNIPPET_NAME: Introspection 101]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Quick example of Python introspection capabilities]
# [SNIPPET_AUTHOR: Gonzalo Núñez <gnunezr@gmail.com>]
# [SNIPPET_LICENSE: GPL]
import types
import sys
import os

def query( item ):
	''' Retrieve all attributes from the given element <item> and display their name and docstring.'''
	if None == item:
		return

	itemDir = dir( item )
	item_name = item.__name__
		
	for elem in itemDir:
		element_name = str(elem)
		elment_doc = ''
		#
		# Get the element
		# this is equivalent to writing: 'element = item.<the value of elem>' (eg. if elem = '__doc__', item.__doc__)
		#
		element = getattr( item, elem )
		#
		# if element has a __name__ attribute, get it and store it in element_name
		# this is equivalent to writing: 'element_name = element.__name__'
		#
		if hasattr( element, '__name__' ):
			element_name = getattr( element, '__name__' )
			element_name = element.__name__
		#
		# if element has a __doc__ attribute, get it and store it in element_doc
		#
		if hasattr( element, '__doc__' ):
			element_doc = element.__doc__

		print
		print "%s.%s [%s]\n\n%s" %( item_name, element_name, type( elem ), element_doc )
		print
		print

query( os )
