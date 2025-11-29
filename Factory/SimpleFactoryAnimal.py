#SIMPLE FACTORY -> FACTORY METHOD

#Abstract Base Classe:

#from abc import ABC

#Classe Abstrata
    # class Animal(ABC)
#Classe Concreta
    # class Animal

#Simple Factory

#Factory Method

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazSom(self):
        pass


