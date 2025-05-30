from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe de base abstraite représentant un animal. Toutes
    les sous-classes doivent implémenter la méthode sound.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite devant être implémentée par
        des sous-classes pour renvoyer le son de l'animal.
        """
        pass
        
class Dog(Animal):
    """
    classe chien qui herite de Animal
    """

    def sound(self):
        """Return le bruit d'un chien qui aboie"""
        return "Bark"
        
class Cat(Animal):
    """Classe chat qui herite de Animal"""
    def sound(self):
        """Return le son d'un chat qui miaule"""
        return "Meow"
