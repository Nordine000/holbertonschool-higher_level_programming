#!/usr/bin/python3
"""
Fonction qui renve la liste des attribut et methode dispo d'un objet
"""


def lookup(obj):
    """
    Renvoie la liste des attribut et methode dispo d'un obj


    Argument:
    l'obj: L'object a chercher

    Renvoie:
    list: la liste des attribut et meth de l'obj
    """
    return dir(obj)
