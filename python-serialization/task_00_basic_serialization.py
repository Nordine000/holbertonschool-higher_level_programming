#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialiser un dictionnaire Python dans un fichier JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charger et désérialiser un fichier JSON dans un dictionnaire Python.
    """
    with open(filename, "r") as d:
        return json.load(d)
