#!/usr/bin/env python3
"""
classe personnalisée
"""
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convertissez un fichier Csv au format json et
    enregistrez le sous le nom data.json

    Return bool vrai si la conversion est reussi sinon faux
    """
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
