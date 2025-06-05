#!/usr/bin/python3
"""
fonction qui ajoute du texte a la fin du fichier txt
et renvoie le nombre de caractere
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
