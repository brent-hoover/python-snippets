#!/usr/bin/env python
#
# [SNIPPET_NAME: Borg]
# [SNIPPET_CATEGORIES: Patterns]
# [SNIPPET_DESCRIPTION: A module providing a basic implementation of the Borg pattern]
# [SNIPPET_AUTHOR: Scott Ferguson <scottwferg@gmail.com>]
# [SNIPPET_LICENSE: GPL]

"""This pattern ensures that all instances of a particular class share the same state"""

class Borg:
    _borg_state = {}

    def __init__(self):
        self.__dict__ = self._borg_state

# Sample code

class MyObject(Borg):
    _someProperty = 0

    @property
    def someProperty(self):
        return self._someProperty

    @someProperty.setter
    def someProperty(self, value):
        self._someProperty = value

if __name__ == '__main__':
    objectA = MyObject()
    objectB = MyObject()

    # Set the property of only object A
    objectA.someProperty = 5

    # Note that both A and B have the same value for someProperty
    print objectA.someProperty
    print objectB.someProperty
