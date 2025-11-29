from animal import Animal

class Gato(Animal):
    def fazSom(self):
        return "Miiiiaaaauuuuuu"

remy = Gato()
remy.fazSom()