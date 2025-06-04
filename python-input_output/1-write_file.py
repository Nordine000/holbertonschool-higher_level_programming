#!/usr/bin/python3
""" def qui ecrit une chaine dans un fcihier texte et return le nbre de char ecrit"""


def write_file(filename="", text=""):
    """
    ouvre un fichier et ecris a l'interieur
    et reurn le nbre de char
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
