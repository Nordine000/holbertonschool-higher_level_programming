#!/usr/bin/python3
"""
Ce fichier définit la classe MyList.
"""

class MyList(list):
    """
    A subclass of list that includes a method to print the list
    in sorted order.
    """

    def print_sorted(self):
        print (sorted(self))
