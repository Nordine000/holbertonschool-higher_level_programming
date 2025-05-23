#!/usr/bin/python3
"""
définit une classe Rectangle avec des attributs de largeur et de hauteur
"""


class Rectangle():
    """Définit un rectangle par sa largeur et sa hauteur"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialiser le rectangle avec la largeur et la hauteur"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Retourne la surface du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne la perimetre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Renvoie chaîne de caractères du rectangle en utilisant #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Retourne rectangle sous forme de chaîne de caractères"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """imprime une meessage lorsqu'une instance de rectangle est sup"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
