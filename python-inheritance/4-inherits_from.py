#!/usr/bin/python3
"""
Verifie si l'objet est une instance de classe
qui a heriter directement ou indirectement de la classe specifier
"""


def inherits_from(obj, a_class):
    """
    Return True i l'objet est une instance de classe qui a heriter
    directement ou indirectement de la classe spécifie
    sinon False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
