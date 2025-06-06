#!/usr/bin/python3
"""
Fonction de creation de la classe Square héritant de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialise une instance Square.

        Arguments:
        size (int): taille du carré.
        Size doit être un entier positif, validé par integer_validator.

        Super() fait en sorte que sqaure herite biend des attributs rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calcule l'aire du carré.
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
