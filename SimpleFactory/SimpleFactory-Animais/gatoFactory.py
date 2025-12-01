from animalFactory import AnimalFactory
from gato import Gato

class GatoFactory(AnimalFactory):
    def criarAnimal(self):
        return Gato()