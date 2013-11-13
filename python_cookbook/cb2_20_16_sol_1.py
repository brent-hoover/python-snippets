# support 2.3, too
try: set
except NameError: from sets import Set as set
# support classic classes, to some extent
import types
def uniques(sequence, skipset):
    for item in sequence:
        if item not in skipset:
            yield item
            skipset.add(item)
import inspect
def remove_redundant(classes):
    redundant = set([types.ClassType])   # turn old-style classes to new
    for c in classes:
        redundant.update(inspect.getmro(c)[1:])
    return tuple(uniques(classes, redundant))
