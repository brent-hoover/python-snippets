"""
Examples of how to turn lists to strings
"""
mylist = ['spam', 'ham', 'eggs']
print ', '.join(mylist)
print '\n'.join(mylist)

#However, this simple method does not work if the list contains non-string objects, such as integers.
#If you just want to obtain a comma-separated string, you may use this shortcut:

list_of_ints = [80, 443, 8080, 8081]
print str(list_of_ints).strip('[]')

print str(list_of_ints)[1:-1]

#Finally, you may use map() to convert each item in the list to a string, and then join them:

print ', '.join(map(str, list_of_ints))
print '\n'.join(map(str, list_of_ints))

