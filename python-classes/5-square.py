#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The Square class includes:
- A private instance attribute `__size` to store the size of the square.
- A constructor to initialize the size with validation.
- A property to retrieve the size.
- A property setter to set the size with validation.
- A method to calculate the area of the square.
- A method to print the square with the character #.
"""
class Square:
    """class defined for square generation
    """
    def __init__(self, size=0):
        self.size = size
 @property
    def size(self):
        """Gets the size of the square."""
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

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size
