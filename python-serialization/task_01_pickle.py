#!/usr/bin/env python3
"""
classe personnalisée
"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        "Afficher les attributs de l'objet"
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialisez l'objet et enregistrez-le dans un fichier"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as ad:
            print(f"Serialization error: {ad}")

    @classmethod
    def deserialize(cls, filename):
        """Désérialiser l'objet d'un fichier"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as ad:
            print(f"Deserialization error: {ad}")
            return None
