#!/usr/bin/python3
"""
Creation de classe basegeometry vide avec message
"""


class BaseGeometry():
    """
    Classe base avec methdode area non implementer et message
    """
    def area(self):
        """
        Génère une exception car la méthode area n'est pas implémentée.

        Génère:
        Exception: avec le message «area() n'est pas implémenté».
        """
        raise Exception("area() is not implemented")
