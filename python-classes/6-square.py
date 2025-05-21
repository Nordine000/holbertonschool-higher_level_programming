#!/usr/bin/python3
"""
classe carrer avec attribut priver size avec validation de taille
"""


class Square():
    """ la classe qui definis carrer avec un attribut privez"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """obtien la position du carrer"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        -----------
        value : tuple
            A tuple of 2 positive integers.

        Raises:
        -------
        TypeError:
            If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
