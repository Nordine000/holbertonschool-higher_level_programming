#!/usr/bin/python3
"""
Creation de classe basegeometry vide avec message
"""


class BaseGeometry:
    """
    Classe baseGeometrie
    """
    def area(self):
        """
        Génère une exception car la méthode area n'est pas implémentée.

        Génère:
        Exception: avec le message «area() n'est pas implémenté».
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que 'value' est un entier strictement positif.

        Arguments:
        name (str): Nom du paramètre (toujours une chaîne).
        value (int): Valeur à vérifier.

        Exceptions:
        - TypeError : si 'value' n'est pas un entier.
        - ValueError : si 'value' est inférieur ou égal à 0.
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
