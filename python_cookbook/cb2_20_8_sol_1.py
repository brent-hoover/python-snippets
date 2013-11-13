def add_method_to_objects_class(object, method, name=None):
    if name is None:
        name = method.func_name
    class newclass(object.__class__):
        pass
    setattr(newclass, name, method)
    object.__class__ = newclass
import inspect
def _rich_str(self):
    pieces = []
    for name, value in inspect.getmembers(self):
        # don't display specials
        if name.startswith('__') and name.endswith('__'):
            continue
        # don't display the object's own methods
        if inspect.ismethod(value) and value.im_self is self:
            continue
        pieces.extend((name.ljust(15), '\t', str(value), '\n'))        
    return ''.join(pieces)
def set_rich_str(obj, on=True):
    def isrich():
        return getattr(obj.__class__.__str__, 'im_func', None) is _rich_str
    if on:
        if not isrich():
            add_method_to_objects_class(obj, _rich_str, '__str__')
        assert isrich()
    else:
        if not isrich():
            return
        bases = obj.__class__.__bases__
        assert len(bases) == 1
        obj.__class__ = bases[0]
        assert not isrich()
