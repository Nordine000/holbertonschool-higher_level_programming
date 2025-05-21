#!/usr/bin/python3
"""
classe carrer avec attribut priver size avec validation de taille
"""


class Square():
    """ la classe qui definis carrer avec un attribut privez"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
