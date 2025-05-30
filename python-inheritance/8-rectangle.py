#!/usr/bin/python3
"""
Creation de classe Rectangle qui herite de classe basegeo
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Import de la classe basegeo dans le fichier 7
"""


class Rectangle(BaseGeometry):
    """
    Classe rectangle qui herite de la classe basegeo
    """
    def __init__(self, width, height):
        """
        Initialise une instance de Rectangle.

        Arguments:
        width (int): largeur du rectangle.
        height (int): hauteur du rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
