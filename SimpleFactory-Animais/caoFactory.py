from animalFactory import AnimalFactory
from cao import Cao

class CaoFactory(AnimalFactory):
    def criarAnimal(self):
        return Cao()