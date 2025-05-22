#!/usr/bin/python3
"""
définit une classe Rectangle avec des attributs de largeur et de hauteur
"""


class Rectangle():
    """Définit un rectangle par sa largeur et sa hauteur"""
    def __init__(self, width=0, height=0):
        """Initialiser le rectangle avec la largeur et la hauteur"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupérer la largeur"""
        return self.__width

    @width.setter
    def width(self, value):
        """Définir la largeur avec validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupérer la hauteur"""
        return self.__height

    @height.setter
    def height(self, value):
        """Fixer la hauteur avec validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
