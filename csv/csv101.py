#!/usr/bin/env python
#
# [SNIPPET_NAME: CSV 101]
# [SNIPPET_CATEGORIES: csv]
# [SNIPPET_DESCRIPTION: Basic CSV file reading example]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how the basics on how to read CSV files using
# the Python csv module.
# The full documentation for the csv module is available here:
# http://docs.python.org/library/csv.html
#
# The data used in the companion csv101.csv file was taken from here:
# http://www.trainweb.org/tubeprune/Statistics.htm
# See, you can even learn some interesting facts about the London Underground
# network while learning Python.

#
# First things first, we need to import the csv module
# Also import sys to get argv[0], which holds the name of the script
#
import csv
import sys

# Derive the name of the CSV file from the name of the script and initialise
# the content list
csvFile = sys.argv[0].replace('.py', '.csv')
content = []

print('Reading file %s' % csvFile)
# And the rest is really easy as csv.reader can be iterated upon
reader=csv.reader(open(csvFile))
for row in reader:
    """
    For each row, we append the row to the content list, which will
    produce a list of lists.
    """
    content.append(row)
print content

