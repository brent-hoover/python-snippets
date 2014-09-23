my_items = [1, 2, 3, 4, 5]

for myi in my_items:
    if isinstance(myi, basestring):
        print('is a string')
        break
else:
    print('no items are strings')