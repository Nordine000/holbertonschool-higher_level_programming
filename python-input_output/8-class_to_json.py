#!/usr/bin/python3
"""
retourne la description sous forme de dictionnaire avec
"""


def class_to_json(obj):
    """
    __dict__ ser a stocker les attribut spe a une
    instance d'un objet python
    """
    return obj.__dict__
