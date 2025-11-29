from animalFactory import AnimalFactory
from pato import Pato

class PatoFactory(AnimalFactory):
    def criarAnimal(self):
        return Pato()