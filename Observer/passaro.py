from sujeito import Sujeito
from observador import Observador

class SujeitoPassaro(Sujeito):

    def __init__(self, nome):
        self.nome = nome
        self.observadores = []

    def adicionarobservdor(self, observador: Observador):
        self.observadores.append(observador)

    def removerobservador(self, observador: Observador):
        self.observadores.remove(observador)

    def notificarObservadores(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)
