from SimpleFactoryAnimal import Animal
from SimpleFactoryCao import Cao
from SImpleFactoryGato import Gato

class AnimalFactory:
    @staticmethod
    def criarAnimal(animalType: str):
        if animalType == "cao":
            return Cao()
        elif animalType == "gato":
            return Gato()
        else:  raise ValueError(f"Tipo de animal não conhecido: {animalType}")
