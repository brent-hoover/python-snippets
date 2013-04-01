"""A version of isinstance that handles module reload()s better."""
import inspect, types

def obj_signature(obj):
    try:
        filename = inspect.getsourcefile(obj)
        lines, lineno = inspect.findsource(obj)
    except TypeError:
        filename, lineno = '__builtin__', None
    return (obj.__name__, filename, lineno)

def new_isinstance(obj, class_or_classes):
    # fall back to real isinstance for these
    if not hasattr(obj, '__class__'):
        return isinstance(obj, class_or_classes)

    if isinstance(class_or_classes, (tuple, list)):
        classes = class_or_classes
    else:
        classes = [class_or_classes]

    all_sigs = map(obj_signature, classes)

    for ancestor in inspect.getmro(obj.__class__):
        sig = obj_signature(ancestor)
        if sig in all_sigs:
            return True

    return False
