#!/usr/bin/python3

def write_file(filename="", text=""):
     """»Ouvrir et Ã©crire du texte dans un fhier"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
