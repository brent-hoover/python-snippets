def all_descendants(class_object, _memo=None):
    if _memo is None:
        _memo = {}
    elif class_object in _memo:
        return
    yield class_object
    for subclass in class_object.__subclasses__():
        for descendant in all_descendants(subclass, _memo):
            yield descendant
