#!/usr/bin/python3
""" def qui sert a ouvrir un fichier texte et a le lire"""


def read_file(filename=""):
    """
    ouvre le fichier filename
    """
    with open(filename, "r", encoding='utf-8') as f:
        """
        ouvre le fciheir filename et l'imprime et le lis
        """
        print(f.read())
