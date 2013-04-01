#!/usr/bin/env python
#
# [SNIPPET_NAME: vmstat Reader]
# [SNIPPET_CATEGORIES: csv]
# [SNIPPET_DESCRIPTION: Custom CSV reader to read files like vmstat output]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how to use the csv module with a custom separator
# in order to read space separated value files such as the output of the
# vmstat command.
# The full documentation for the csv module is available here:
# http://docs.python.org/library/csv.html
#
# The data used in the companion vmstat.log file was taken bu running the command:
# vmstat -n 5

#
# First things first, we need to import the csv module
# Also import sys to get argv[0], which holds the name of the script
#
import csv
import sys

# Derive the name of the CSV file from the name of the script
csvFile = sys.argv[0].replace('-reader.py', '.log')

# Create a map from minor to major header as the minor headers are easy to
# associate to columns, which is not the case for major headers.
minor2major = {
    'r': 'procs',
    'b': 'procs',
    'swpd': 'memory',
    'free': 'memory',
    'buff': 'memory',
    'cache': 'memory',
    'inact': 'memory',  # to support the vmstat -a option if required
    'active': 'memory', # to support the vmstat -a option if required
    'si': 'swap',
    'so': 'swap',
    'bi': 'io',
    'bo': 'io',
    'in': 'system',
    'cs': 'system',
    'us': 'cpu',
    'sy': 'cpu',
    'id': 'cpu',
    'wa': 'cpu'
}
minors = []

# Initialise the content map by creating an empty sub-map against each
# unique major header
content = dict([(h, {}) for h in set(minor2major.values())])

print('Reading file %s' % csvFile)
# Create the reader and specify the delimier to be a space; also set the
# skipinitialspace flag to true to ensure that several spaces are seen as a
# single delimiter and that initial spaces in a line are ignored
reader=csv.reader(open(csvFile), delimiter=' ', skipinitialspace=True)
for row in reader:
    if reader.line_num == 1:
        """
        Ignore the first line as it contains major headers.
        """
    elif reader.line_num == 2:
        """
        If we are on the first line, create the headers list from the first row.
        We also keep a copy of the minor headers, in the order that they appear
        in the file to ensure that we can map the values to the correct entry
        in the content map.
        """
        minors = row
        for h in row:
            content[minor2major[h]][h] = []
    elif row[0] != minors[0] and row[0] != minor2major[minors[0]]:
        """
        If the -n option was not specified when running the vmstat command,
        major and minor headers are repeated so we need to ensure that we
        ignore such lines and only deal with lines that contain actual data.
        For each value in the row, we append it to the respective entry in
        the content dictionary. In addition, we transform the value to an int
        before appending it as we know that the content of the log should only
        have integer values.
        """
        for i, v in enumerate(row):
            content[minor2major[minors[i]]][minors[i]].append(int(v))

print "\nThe minor headers read from the file"
print minors
print "\nThe CPU user process stats"
print content['cpu']['us']
print "\nMinimum free memory in the data set"
print min(content['memory']['free'])
print "\nMaximum IO, either input or output"
print max([max(l) for l in content['io'].values()])

