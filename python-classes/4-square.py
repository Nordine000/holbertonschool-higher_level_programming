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

    @property
    def size(self):
        """
         Obtention de l'attribut size.

        Retourne :
            int : la taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Paramètre pour l'attribut size avec validation.

        Args :
            value (int) : La nouvelle valeur de la taille.

        L'erreur est levée :
            TypeError : Si size n'est pas un entier.
            ValueError : Si la taille est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
