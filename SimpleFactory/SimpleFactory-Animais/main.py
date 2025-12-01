from gatoFactory import GatoFactory
from caoFactory import CaoFactory
from patoFactory import PatoFactory

animal1 = GatoFactory.criarAnimal("gato")
print(animal1.fazSom())

animal2 = CaoFactory.criarAnimal("cao")
print(animal2.fazSom())

animal3 = PatoFactory.criarAnimal("pato")
print(animal3.fazSom())