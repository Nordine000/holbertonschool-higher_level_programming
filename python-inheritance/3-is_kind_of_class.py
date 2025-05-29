#!/usr/bin/python3
"""
Fonction qui renvoie true si l'obj est une instance de classe spe sinon false
"""


def is_kind_of_class(obj, a_class):
    """
    Renvoie True si obj est une instance de a_class ou une instance d'une
    classe héritée de a_class; sinon False.

    Arguments:
    obj: L'objet à vérifier.
    a_class: La classe à comparer.

    Renvoie:
    bool: True si obj est une instance de a_class ou
    une sous-classe de a_class, sinon False.
    """
    return isinstance(obj, a_class)
