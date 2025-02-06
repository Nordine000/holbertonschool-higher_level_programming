#!/usr/bin/python3
'''
classe Rectangle qui hérite de BaseGeometr
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    classe rectangle qui herite de Base
    """
    def __init__(self, width, height):
        """
        init un rctangle avc une largeur et une hauteur

        Para:
        width : int (largeur du rectangle)
        height : int (hauteur du rectangle)
        """
        self.__width = None
        self.__height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
