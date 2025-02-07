#!/usr/bin/python3
'''
classe Square qui hérite deRectangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    classe square qui herite de rectangle
    """
    def __init__(self, size):
        """
        init de size

        Para:
        size :int
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        methode qui calcule et retourne size
        """
        return self.__size * self.__size
