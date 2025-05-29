#!/usr/bin/python3
"""
Fonction qui renvoie true si l'obj est une instace d'une classe heriter
direct ou indirect de la calsse spe sinon false
"""


def inherits_from(obj, a_class):
    """
    Renvoie True si l'objet est une instance d'une classe héritée
    (directement ou indirectement) de la classe spécifiée; sinon False.

    Arguments:
    obj: L'objet à vérifier.
    a_class: La classe à comparer.

    Renvoie:
    bool: True si obj est une instance d'une sous-classe de a_class
    (à l'exclusion de la classe elle-même), sinon False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
