#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get all properties of a class
"""


def iter_properties_of_class(cls):
    for varname in vars(cls):
        value = getattr(cls, varname)
        if isinstance(value, property):
            yield varname

def properties(inst):
    result = {}
    for cls in inst.__class__.mro():
        for varname in iter_properties_of_class(cls):
            result[varname] = getattr(inst, varname)
    return result

>>> a = MyClass()
>>> a.x = 5
Setting x to 5
>>> properties(a)
{'x': 5}

class MyClass(object):
    @property
    def x(self):
        pass

class MyDataClass(object):

    def __init__(self):
        self.value1 = None
        self.value2 = None

    def __iter__(self):
        for varname in vars(self):
            yield varname


# this get the names of properties including __dunder__ types
print vars(MyClass).keys()
mdc = MyDataClass()
for x in mdc:
    print(x)

