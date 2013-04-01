#!/usr/bin/env python
#
# [SNIPPET_NAME: Dictionaries 101]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Basic and not so basic dictionary operations]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how the basics on dictionaries: how to create, add,
# remove items, get items, iterate, etc.

#
# First, let's create simple dictionary. A dictionary (called map in Java hash
# in perl) is similar to a list with the difference that the key doesn't
# have to be an integer, it can be anything.
#
# A dictionary is enclosed in curly brackets and each key is mapped to its
# corresponding value with a colon. So in the dictionary below, we associate
# the key Karmic with the value 9.10 and so on for the 5 pairs.
#
print "Create a simple dictionary"
simpleDict = {"Karmic": "9.10", "Lucid": "10.04", "Hardy": "7.10",
              "Jaunty": "8.10", "Intrepid": "8.04"}
# print it
print simpleDict
#
# Another way to create a dictionary is to zip two lists containing the keys
# and values in the same order to create a list of tuples, which we can then
# pass to the dict() method to create a dictionary.
#
myKeys = ['Feisty', 'Edgy', 'Dapper']
myValues = ['7.04', '6.10', '6.06']
otherDict = dict(zip(myKeys, myValues))
print otherDict
#
# Interrogate the dictionary. It works exactly the same as with a list, with the
# exception that the key is no longer an integer.
#
print "\nInterrogate the dictionary"
# get for value for key Jaunty
print simpleDict['Jaunty']
# get the length of the dictionary
print len(simpleDict)
# check if the dictionary contains the key Lucid
print 'Lucid' in simpleDict
print 'Breezy' in simpleDict
#
# Modify the dictionary
#
print "\nModify the dictionary"
# add another item
simpleDict['Hoary'] = '5.06'
print simpleDict
# oops! let's sort this out by replacing in place
simpleDict['Hoary'] = '5.04'
print simpleDict
# update the dictionary with mappings from another one
simpleDict.update(otherDict)
print simpleDict
# remove an item from the list (Hardy should not be in the list anymore)
del simpleDict['Hoary']
print simpleDict
#
# Iterate over the dictionary. A dictionary doesn't enforce a natural ordering
# like a list but we can still iterate over it in multiple ways.
# However, note that when you iterate, the order in which the items are
# retrieved is unspecified.
#
print "\nIterate over the dictionary"
print "\nby keys"
for k in simpleDict.keys():
    print k
print "\nby values"
for v in simpleDict.values():
    print v
print "\nby items"
# note the syntax to retrieve the key and value at the same time
for k, v in simpleDict.items():
    print k, '=>', v
#
# More interesting transformations from list to dictionary and vice versa.
# List comprehension allow you to do a lot of interesting stuff, in particular
# tranforming lists into dictionaries and the other way around.
#
print "\nList to dictionary and vice versa"
# First, let's transform our dictinary into a list of tuples
simpleList = [(k, v) for k, v in simpleDict.items() ]
print simpleList
# Create a map from a list with the list's entry as key and the index as value
# This method takes advantage of another way of creating a map, using a
# sequence of tuples, so in practice, we create a tuple for each item in the
# list, create a list from all the tuples using a list comprehension and pass
# it as argument to the dict() function
cityList = ['London', 'Paris', 'New York', 'Tokyo']
cityDict = dict([(x, i) for i, x in enumerate(cityList)])
print cityDict
# Create a map from a number to its square
squareDict = dict([(x, x * x) for x in range(1, 10)])
print squareDict

