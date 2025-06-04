#!/usr/bin/python3
""" def qui sert a ouvrir un fichier texte et a le lire"""


def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read())
