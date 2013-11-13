"""
params is a string of the class that you want
example:
my_class = "do_something"
instance = factory(my_class)
the name module is hard coded ...
"""

def factory(cls_string, *args):
    cls = getattr(module, cls_string)
    return apply(cls, args)');
