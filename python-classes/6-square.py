#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The Square class includes:
- A private instance attribute `__size` to store the size of the square.
- A private instance attribute `__position` to store the position of
the square.
- A constructor to initialize the size and position with validation.
- A property to retrieve the size.
- A property setter to set the size with validation.
- A property to retrieve the position.
- A property setter to set the position with validation.
- A method to calculate the area of the square.
- A method to print the square with the character #.
"""
class Square:
    """class defined for square generation
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
