#!/usr/bin/env python3
"""
basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and
deserialize the JSON file to recreate the Python Dictionary.
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Sérialise les données et les sauvegarde dans unichier
    """
    with open(filename, 'wb') as fichier:
        pickle.dump(data, fichier)
    pass


def load_and_deserialize(filename):
    """
    desérialise les données et les sauvegarde da un fichi
    """
    with open(filename, "rb") as f:
        deserialized_dict = pickle.load(f)
        return deserialized_dict
    pass
