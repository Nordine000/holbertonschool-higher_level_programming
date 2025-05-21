#!/usr/bin/python3
"""
classe carrer avec attribut priver size avec validation de taille
"""


class Square():
    """ la classe qui definis carrer avec un attribut privez"""
    def __init__(self, size=0):
        self.size = size

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
        self.__size = value

    def area(self):
        """ Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """ Imprime le carré en utilisant le caractère '#' """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
