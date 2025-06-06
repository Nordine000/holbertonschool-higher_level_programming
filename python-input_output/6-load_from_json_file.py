#!/usr/bin/python3
"""
fonction qui return un obj creer un objet a partir d'un
fichier json(ex: dico a list)
"""
import json


def load_from_json_file(filename):
    """
    cree un objet a partir d'un fichier json
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
