#!/usr/bin/python3
'''
class student
'''


class Student:
    """definit un etudiant avec son prenom, son nom et son age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Recupere une representation de dico d'une instance student"""
        return self.__dict__
