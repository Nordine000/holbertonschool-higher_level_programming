#!/usr/bin/python3
"""
Creation de la classe mylist qui herite de list
"""


class MyList(list):
    """
    imprime une liste en ordre croissant
    """
    def print_sorted(self):
        print(sorted(self))
