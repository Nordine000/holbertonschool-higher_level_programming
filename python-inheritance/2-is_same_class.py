#!/usr/bin/python3
"""
Fonction qui renvoie true si l'obj est une instance de classe spe sinon false
"""


def is_same_class(obj, a_class):
    """
    Renvoie True si obj est une instance exacte de a_class, sinon False.

    Arguments:
    obj: L'objet à vérifier.
    a_class: La classe à comparer.

    Renvoie:
    bool: True si obj est une instance exacte de a_class, sinon False.
    """
    return type(obj) is a_class
