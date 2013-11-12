#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyPropertyDescriptor(object):
    """
    This object defines how the property "neighborhoods" will be used on
    any object that uses it.
    """

    def __get__(self, instance, owner):
        # Use a private variable to avoid calling the getter recursively
        if hasattr(instance, '_greetings'):
            return instance._greetings
        else:
            return None

    def __set__(self, instance, value):
    # Custom code can go here to transform the value on set
    # Code is slightly naive since it assume value is string
        instance._greetings = value.upper()

    def __delete__(self, instance):
        del instance._neighborhoods


class ObjectWithDescriptor(object):
    neighborhoods = MyPropertyDescriptor()

    def __init__(self):
        self.other_property = None

    def print_values(self):
        print(self.neighborhoods)
        print(self.other_property)

if __name__ == '__main__':
    owd = ObjectWithDescriptor()
    owd.print_values()
    owd.neighborhoods = 'hello monkey'
    owd.other_property = 'hello banana'
    owd.print_values()
