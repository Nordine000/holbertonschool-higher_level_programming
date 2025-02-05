#!/usr/bin/python3
"""
verifie si l'objet est une instance de class
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instance de la classe spécifie,
    sinon False

    Parameters:
    obj : object L'objet vérifir
    a_class : type
        La classe comparer avec le type de l'objet
    Returns:
    bool
    True si l'objet est exactement une instance de a_class,
        sinon False
        """
    return type(obj) is a_class
