#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The Square class includes:
- A private instance attribute `__size` to store the size of the square.
- A constructor to initialize the size with validation.
- A property to retrieve the size.
- A property setter to set the size with validation.
- A method to calculate the area of the square.
"""

class Square:
    """class defined for square generation
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
