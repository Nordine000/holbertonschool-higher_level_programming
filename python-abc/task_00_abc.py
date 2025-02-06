#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite
    """
    @abstractmethod
    def sound(self):
        """
    Methode abstraite a implementer sous classe
    """
        pass


class Dog(Animal):
    """
    classe chien
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    classe chat
    """
    def sound(self):
        return "Meow"
