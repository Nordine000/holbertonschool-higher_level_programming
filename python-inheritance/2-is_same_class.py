#!/usr/bin/python3
"""
Fonction qui renvoie true si l'obj est une instance de classe spe sinon false
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
