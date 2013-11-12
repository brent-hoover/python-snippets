# [SNIPPET_NAME: Filter, Map & Reduce of lists]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: Simple examples to show common features in everyday work with lists]
# [SNIPPET_AUTHOR: Benjamin Klueglein <scheibenkaes@googlemail.com>]
# [SNIPPET_LICENSE: GPL]

numbers = range(1, 20, 1) # Numbers from 1 to 20
#########################
# Filtering of lists:
#	Pick a amount of items which match a certain condition
#########################
# e.g. Get all odd numbers
odd_numbers = filter(lambda n: n % 2, numbers)
print odd_numbers
# prints [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#########################

#########################
# Mapping of lists:
# 	Apply a function to each item and return the result of each invocation in a list
#########################
# Calculate the square of two for each number
squared_numbers = map(lambda n: n ** 2, numbers)
# Alternate approach:
squared_numbers = [n ** 2 for n in numbers]
print squared_numbers
# prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
#########################

#########################
# Reducing of lists
#	 Apply a function of two arguments cumulatively to the items of a sequence,
#    from left to right, so as to reduce the sequence to a single value.
#	 (Taken from reduce docstring)
#########################
# Sum up all numbers
sum_of_numbers = reduce(lambda n, m: n + m, numbers)
print sum_of_numbers
# prints 190
#########################
