#!/usr/bin/python3
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass
def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(list)
