#!/usr/bin/python3
"""
fonction qui return represnetation d'un obj
sous forme de chaine de char
"""
import json
""" importation du module json"""


def to_json_string(my_obj):
    """json dumps sert a encoder/tranfromer un objet(dico/liste) en une chaine
    de char JSON
    """
    return json.dumps(my_obj)
