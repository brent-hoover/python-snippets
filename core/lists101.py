#!/usr/bin/env python
#
# [SNIPPET_NAME: Lists 101]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Basic and not so basic list operations]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how the basics on lists: how to create, add,
# remove items, get items or slices, sort, etc.

#
# First, let's create simple list
#
print "Create a simple list"
simpleList = ["Karmic", "Lucid", "Hardy", "Jaunty", "Intrepid"]
# print it
print simpleList
#
# Interrogate the list
#
print "\nInterrogate the list"
# get item 3:  lists start counting at 0 so it should be Jaunty
print simpleList[3]
# we can also get a slice
print simpleList[2:4]
# get the first three items
print simpleList[:3]
# or all items from number index 3 (which is the fourth item) to the end
print simpleList[3:]
# we can also take every other item, as a slice is defined
# like this: start:stop:step
print simpleList[::2]
# get the length of the list
print len(simpleList)
# we can get the index of an item in the list
print simpleList.index("Hardy")
# and when the list doesn't contain the item, we get an error that we can catch
try:
    print simpleList.index("Feisty")
except ValueError:
    print "The list doesn't contain the item Feisty"
#
# Modify the list
#
print "\nModify the list"
# add another item
simpleList.append("Twisty")
print simpleList
# oops! let's sort this out by replacing in place
simpleList[5] = "Gutsy"
print simpleList
# extend the list with another one
otherList = ["Edgy", "Breezy"]
simpleList.extend(otherList)
print simpleList
# remove an item from the list (Hardy should not be in the list anymore)
del simpleList[2]
print simpleList
# insert an item in the middle of the list
simpleList.insert(4, "Hardy")
print simpleList
# remove an item by its value rather than its index
simpleList.remove("Edgy")
print simpleList
#
# Create modified copies of the list
#
print "\nCreate modified copies of the list"
# sort it
print sorted(simpleList)
# join it to produce a custom print
print ' => '.join(sorted(simpleList))
# lists can contain the same item several times so if we add Lucid again:
simpleList.append("Lucid")
# we have it twice in the list (easier to see if we sort it)
print sorted(simpleList)
# but we can get round that by transforming it into a set, which is a list
# with no duplicates; and of course we can also sort the set
print sorted(set(simpleList))
#
# Iterate over the list
#
print "\nIterate over the list"
for i in simpleList:
    print i.upper()
# but if we want to create another list by applying the same expression to
# each item, we can use a list comprehension
upList = [i.upper() for i in sorted(set(simpleList))]
print upList

