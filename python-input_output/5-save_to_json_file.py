#!/usr/bin/python3
'''
enregistrer l'objet dans un fichier
'''
import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier texte à l'aide d'une représentation JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
