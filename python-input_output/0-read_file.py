#!/usr/bin/python3
'''
Ce module contient une fonction read_files
'''


def read_file(filename=""):
    """
    Lit un fichier texte (UTF8) et l'affiche sur stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
