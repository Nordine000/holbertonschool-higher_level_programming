#!/usr/bin/python3
"""
fonction qui return un objet recue et representer par
une chaine de char JSON
"""
import json
"""impor de json"""


def from_json_string(my_str):
    """"loads seert a la conversion inverse, chaine de char json recue
    d'serveur etc... et la transforme en objet python
    """
    return json.loads(my_str)
